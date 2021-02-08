import requests
import time
import os
import json
import subprocess
from loguru import logger

from config import proxies  # if you don't need it, just delete it and its usages

requests.adapters.DEFAULT_RETRIES = 5
SESSION = requests.Session()
SESSION.keep_alive = False
BASE_SLEEP_TIME = 3

user_agent = 'Mozilla/5.0 ven(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

LOG_PATH = 'out/log'
os.makedirs(LOG_PATH, exist_ok=True)
logger.add(LOG_PATH + '/{time}.log')


def send(url, token='', max_retry=1, sleep_time=1):
    time.sleep(BASE_SLEEP_TIME)

    headers = {'User-Agent': user_agent}
    if token:
        headers['Authorization'] = 'token' + token

    try:
        res = SESSION.get(url, headers=headers, stream=False, timeout=10)
        return res
    except Exception as e:
        logger.error('[Request Error] url: {}    - msg: {}'.format(url, e))

        # only retry when exception happens
        if max_retry <= 0:
            return None
        cur_sleep_time = sleep_time + BASE_SLEEP_TIME
        time.sleep(cur_sleep_time)
        return send(url, token, max_retry - 1, sleep_time=cur_sleep_time)


def save(content, path):
    # logger.debug('[Save] {}'.format(path))
    create_missing_dirs(path)
    with open(path, 'w') as f:
        f.write(content)
        f.flush()  # copy data from the program buffer to the operating system buffer
        # os.fsync(f) # write to disk


def exists_file(path):
    return os.path.exists(path)


def load_json_from_file(path: str):
    j = []
    try:
        with open(path, 'r') as f:
            j = json.load(f)
    except Exception as e:
        logger.error('[LOAD JSON ERR] {} : {} '.format(path, e))
    return j


def exe_cmd(cmd: str):
    stat, ouput = subprocess.getstatusoutput(cmd)
    if stat != 0:
        logger.error('[EXE COMMAND ERROR] {}\n{}'.format(cmd, ouput))
    return stat, ouput


def create_missing_dirs(path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)


def rselect(src_file: str, outfile: str, line_num: int):
    '''
        -   Linux
            -   shuf
        -   MacOS
            -   brew install coreutils  
            -   gshuf -n 1000 java_code_overlap_pairs.csv -o java_selected_1000.csv 
    '''
    create_missing_dirs(outfile)
    exe_cmd('gshuf -n {} {} -o {}'.format(line_num, src_file, outfile))
