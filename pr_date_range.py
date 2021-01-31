import json

import utils
from config import token
from datetime import datetime, timedelta
import glob
import re

MAX_TOTAL_NUM = 10000
# MAX_EACH_NUM = 1000
# MIN_STARS = 20  # min star number of a repository
RE_REPO_NAME = re.compile(r'https://api\.github\.com/repos/([^/]+/[^/]+)/')
RE_SHA = re.compile(r'https://github\.com/[^/]+/[^/]+/blob/(\w+)/')


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
    ulink = query + '&page={}&per_page=100'

    for page_cnt in range(1, 11):
        # if pr_cnt >= MAX_EACH_NUM:
        #     break

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
                    # if get_repo_stars(repo_name) <= MIN_STARS:
                    #     continue

                    link_files = item['url'].replace('/issues/', '/pulls/') + '/files\n'
                    file_list.append(link_files)
                    pr_cnt += 1

        if file_list:
            with open(out_path.format(start_date, end_date), 'a+') as outfile:
                outfile.writelines(file_list)
                outfile.flush()

        # break

    utils.logger.warning(f'pr count {pr_cnt}')
    return pr_cnt


def save_files(csv_file: str, language: str):
    '''
    Query links in csv_file and save, and update csv with sha
    :param csv_file: the path to csv files generated by the method search_pr
    :param language: repository language
    :return: none
    '''
    new_csv_lines = list()

    out_path = f'out/{language}/files/'
    with open(csv_file, 'r') as f:
        for line in f:
            link = line.strip()

            savepath = link.replace('https://api.github.com/repos/', out_path) + '.json'

            # json_resp = None
            if utils.exists_file(savepath):  # if file exists, do not send unnecessary request
                with open(savepath, 'r') as jfile:
                    json_resp = json.load(jfile)
            else:
                resp = utils.send(link, token, 3)
                if not resp or resp.status_code != 200:
                    continue
                utils.save(resp.text, savepath)
                json_resp = resp.json()
                # pass

            # Github file status: 'added' , 'modified' , 'removed' , 'renamed'
            # find the fist non-removed status file and extract the sha
            sha = ''
            if json_resp:
                for file in json_resp:
                    if file['status'] != 'removed' and 'blob_url' in file:
                        try:
                            m = RE_SHA.search(file['blob_url'])
                            if m:
                                sha = m.groups()[0]
                                break
                        except TypeError as e:
                            # "blob_url": null
                            utils.logger.error(f'[Sha Error] {savepath}\n{e}')
                            continue
            new_csv_lines.append(f'{line.strip()},{sha}\n')

    with open(csv_file, 'w') as outfile:
        outfile.writelines(new_csv_lines)
        outfile.flush()


def step1():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=1)
    total_cnt = 0
    while total_cnt < MAX_TOTAL_NUM:
        total_cnt += search_pr('java', start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        start_date -= timedelta(days=2)
        end_date -= timedelta(days=2)
    utils.logger.warning(f'total:{total_cnt}')


def step2():
    root = 'out/java/links'
    paths = glob.glob(f'{root}/**/*.csv', recursive=True)
    for p in paths:
        save_files(p, 'java')


def normal_search(language: str):
    out_path = 'out/' + language + '/links/{}.csv'
    utils.create_missing_dirs(out_path)
    pr_cnt = 0

    ulink = f'https://api.github.com/search/issues?q=language:{language}+is:pr+is:open'
    ulink = ulink + '&page={}&per_page=100'

    for page_num in range(1, 11):
        resp = utils.send(ulink.format(page_num), token, 3)
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

                    link_files = item['url'].replace('/issues/', '/pulls/') + '/files\n'
                    file_list.append(link_files)
                    pr_cnt += 1

        if file_list:
            with open(out_path.format(page_num), 'a+') as outfile:
                outfile.writelines(file_list)
                outfile.flush()

        # break

    utils.logger.warning(f'pr count {pr_cnt}')


if __name__ == '__main__':
    # step1()
    # normal_search('java')
    step2()
