"""
Get top-100 repositories sorted by stars, and sort by size
"""
import utils
from config import token
import json

path_top_100_stars = 'spotbugs-experiment/top-100-stars.json'
path_sort_size = 'spotbugs-experiment/sort-size.json'


def get_top_100_stars():
    query = 'https://api.github.com/search/repositories?q=language:java&page=1&per_page=100'
    resp = utils.send(query, token, 3)
    if not resp:
        print("No response")
        exit(1)

    jresp = resp.json()

    utils.create_missing_dirs(path_top_100_stars)
    with open(path_top_100_stars, 'w') as out:
        json.dump(jresp, out)


def sort_by_size():
    with open(path_top_100_stars, 'r') as f:
        jlist = json.load(f)

    jlist = jlist['items']

    sorted_list = sorted(jlist, key=lambda k: k.get('size', 0))

    simple_list = [{
        'html_url': repo['html_url'],
        'stargazers_count': repo['stargazers_count'],
        'size': repo['size']
    } for repo in sorted_list]

    utils.create_missing_dirs(path_sort_size)
    with open(path_sort_size, 'w') as out:
        json.dump(simple_list, out)


if __name__ == '__main__':
    get_top_100_stars()
    sort_by_size()
