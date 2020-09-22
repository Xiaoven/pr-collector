# import utils
# import json
# from config import token
#
# if __name__ == "__main__":
#     keys = {'bad+practice'}
#     languages = ['Java']
#     ulink = 'https://api.github.com/search/issues?q=%22{}%22+language:{}+is%3Apr+is%3Aclosed&page={}&per_page=100'
#
#     for language in languages:
#         for key in keys:
#             for cnt in range(1, 101):
#                 resp = utils.send(ulink.format(key, language, str(cnt)), token, 3)
#                 if not resp or resp.status_code != 200:
#                     break
#
#                 jresp = resp.json()
#
#                 if 'items' in jresp:
#                     # store page
#                     out_path = 'out/{}/{}.json'.format(language, str(cnt))
#                     utils.create_missing_dirs(out_path)
#                     item_list = []
#
#                     for item in jresp['items']:
#                         obj = {'url':'', 'comments':0, 'title':'', 'body':''}
#
#                         if 'url' in item:
#                             obj['url'] = item['url']
#                         if 'comments' in item:
#                             obj['comments'] = item['comments']
#                         if 'title' in item:
#                             obj['title'] = item['title']
#                         if 'body' in item:
#                             obj['body'] = item['body']
#
#                         item_list.append(obj)
#
#                     with open(out_path, 'w') as outfile:
#                         json.dump(item_list, outfile)
#
