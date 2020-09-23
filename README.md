## Github API
[Query for values between a range](https://docs.github.com/en/github/searching-for-information-on-github/understanding-the-search-syntax#query-for-values-between-a-range)

[Searching issues and pull requests](https://docs.github.com/en/github/searching-for-information-on-github/searching-issues-and-pull-requests)

## Requests
**Main Problem**: `HTTPSConnectionPool: Max retries exceeded with url`

[set stream parameter to False](https://2.python-requests.org/en/master/user/advanced/#body-content-workflow)

[keep-alive is automatic within a session](https://2.python-requests.org/en/master/user/advanced/#keep-alive)

## Getting Start
1. add `config.py`
```python
token = 'YOUR TOKEN'
proxies = {} # YOUR Proxy
```

2. set `MAX_TOTAL_NUM`, `MAX_EACH_NUM ` and `MIN_STARS` at `pr_date_range.py` as you need.