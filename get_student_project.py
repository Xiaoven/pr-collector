import utils
from config import token

if __name__ == '__main__':
    save_path = 'student_repos/'
    utils.create_missing_dirs(save_path)

    max_num = 20
    cur_num = 0

    # link1 = 'https://api.github.com/search/repositories?q=course+project+language:java+stars:0..10+size:900..5000&per_page=100&page='
    link1 = 'https://api.github.com/search/repositories?q=language:java+stars:400..1000+size:900..5000&per_page=100&page='
    page_num = 0
    while page_num <= 10:
        page_num += 1

        resp = utils.send(link1 + str(page_num), token, 3)
        if not resp or resp.status_code != 200:
            break

        with open(save_path + 'star' + str(page_num) + '.json', 'w') as f:
            f.write(resp.text)

        jresp = resp.json()
        for item in jresp['items']:
            html_url = item['html_url']
            description = item['description']

            if 'android' in html_url.lower():
                continue
            if description and 'android' in description.lower():
                continue

            # if repo contains pom.xml or build.gradle file, without apps directory
            contents_link = html_url.replace('https://github.com', 'https://api.github.com/repos') + '/contents'
            cnt_resp = utils.send(contents_link, token, 3)
            if not cnt_resp or cnt_resp.status_code != 200:
                continue

            contain_app = False
            contain_pom = False
            contain_gradle = False
            for content in cnt_resp.json():
                if content['name'] == 'app' and content['type'] == 'dir':
                    contain_app = True
                    break
                elif content['name'] == 'pom.xml':
                    contain_pom = True
                elif content['name'] == 'build.gradle':
                    contain_gradle = True

            if not contain_app and (contain_gradle or contain_pom):
                with open(save_path + 'star_rst.txt', 'a') as f:
                    f.write(html_url + '\n')
                cur_num += 1

            if cur_num >= max_num:
                break
        if cur_num >= max_num:
            break




