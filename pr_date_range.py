import utils
from config import token
from datetime import datetime, timedelta
import glob
import re

MAX_TOTAL_NUM = 2000
MAX_EACH_NUM = 200
MIN_STARS = 20 # min star number of a repository
RE_REPO_NAME = re.compile('https://api\.github\.com/repos/([^/]+/[^/]+)/')


def get_repo_stars(repo_name: str):
    '''
    return the number of stars given repository name
    :param repo_name: string
    :return: the number of stars
    '''
    ulink = f'https://api.github.com/repos/{repo_name}'
    resp = utils.send(ulink, token, 3)
    if not resp or resp.status_code != 200:
        return -1
    return resp.json()['stargazers_count']


def get_repo_name(pr_link: str):
    m = RE_REPO_NAME.search(pr_link)
    if not m:
        return None
    return m.groups()[0]


def search_pr(language: str, start_date: str, end_date=''):
    '''
    Query pull requests created from start_date to end_date, and save links to files in csv tables
    :param language: repository language
    :param start_date: string in the format of YYYY-MM-DD
    :param end_date: string in the format of YYYY-MM-DD
    :return: the number of pull requests
    '''
    out_path = 'out/' + language + '/links/{}_{}.csv'
    utils.create_missing_dirs(out_path)
    pr_cnt = 0

    # ulink example: https://api.github.com/search/issues?q=language:Java+is:pr+is:open+created:2020-09-10..2020-09-15
    query = f'https://api.github.com/search/issues?q=language:{language}+is:pr+is:open+created:{start_date}'
    if end_date:
        query += f'..{end_date}'
    ulink = query + 'c'

    for page_cnt in range(1, 101):
        if pr_cnt >= MAX_EACH_NUM:
            break

        resp = utils.send(ulink.format(page_cnt), token, 3)
        if not resp or resp.status_code != 200:
            break
        jresp = resp.json()

        file_list = []
        if 'items' in jresp:
            for item in jresp['items']:
                if 'url' in item:
                    repo_name = get_repo_name(item['url'])
                    if not repo_name:
                        continue  # If it works fine, this line wont be executed
                    if get_repo_stars(repo_name) <= MIN_STARS:
                        continue

                    link_files = item['url'].replace('/issues/', '/pulls/') + '/files\n'
                    file_list.append(link_files)
                    pr_cnt += 1

        if file_list:
            with open(out_path.format(start_date, end_date), 'a+') as outfile:
                outfile.writelines(file_list)
                outfile.flush()

        break

    utils.LOGGER.warning(f'pr count {pr_cnt}')
    return pr_cnt


def save_files(csv_file: str, language: str):
    '''
    Query links in csv_file and save
    :param csv_file: the path to csv files generated by the method search_pr
    :param language: repository language
    :return: none
    '''
    out_path = f'out/{language}/files/'
    with open(csv_file, 'r') as f:
        for line in f:
            link = line.strip()

            savepath = link.replace('https://api.github.com/repos/', out_path) + '.json'
            if utils.exists_file(savepath):  # if file exists, do not send unnecessary request
                continue

            resp = utils.send(link, token, 3)
            if not resp or resp.status_code != 200:
                continue
            utils.save(resp.text, savepath)


def step1():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    total_cnt = 0
    while total_cnt < MAX_TOTAL_NUM:
        total_cnt += search_pr('java', start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        start_date -= timedelta(days=31)
        end_date -= timedelta(days=31)
    utils.LOGGER.warning(f'total:{total_cnt}')


def step2():
    root = 'out/java/links'
    paths = glob.glob(f'{root}/**/*.csv', recursive=True)
    for p in paths:
        save_files(p, 'java')


if __name__ == '__main__':
    # step1()
    step2()
