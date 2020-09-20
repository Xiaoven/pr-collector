import utils
from tokens import token

if __name__ == '__main__':
    languages = ['Java']

    # Step 1: get links
    # ulink = 'https://api.github.com/search/issues?q=language:{}+is%3Apr+is%3Aopen&page={}&per_page=100'
    #
    # for language in languages:
    #     out_path = 'out/prs/{}.csv'.format(language)
    #     utils.create_missing_dirs(out_path)
    #
    #     for cnt in range(1,2):
    #         resp = utils.send(ulink.format(language, str(cnt)), token, 3)
    #         if not resp or resp.status_code != 200:
    #             break
    #         jresp = resp.json()
    #
    #         if 'items' in jresp:
    #             file_list = []
    #             for item in jresp['items']:
    #                 if 'url' in item:
    #                     link_files = item['url'].replace('/issues/', '/pulls/') + '/files\n'
    #                     file_list.append(link_files)
    #
    #             with open(out_path, 'a+') as outfile:
    #                 outfile.writelines(file_list)

    # Step 2: save files
    for language in languages:
        links_path = 'out/prs/{}.csv'.format(language)
        with open(links_path, 'r') as f:
            for line in f:
                link = line.strip()

                savepath = link.replace('https://api.github.com/repos/', f'download/{language}/') + '.json'
                if utils.exists_file(savepath):
                    continue

                resp = utils.send(link, token, 3)
                if not resp or resp.status_code != 200:
                    continue

                utils.save(resp.text, savepath)
