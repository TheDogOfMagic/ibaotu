# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq
import re

def load_cookies(file):
    cookies = {}
    with open(file, 'r') as f:
        list_str = f.read()
    pattern = re.compile('"name": "(.*?)",.*?"value": "(.*?)"', re.S)
    items = re.findall(pattern, list_str)
    for item in items:
        cookies[item[0]] = item[1]
    return cookies

# def get_url(url):
#     cookies = load_cookies('cookies.txt')
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
#     }
#     print('合成url：', url)
#     response = requests.get(url)
#     if response.text:
#         print('请求后url:', response.url)
#
#         return response.url
#     else:
#         return None
def get_download_url(url):
    cookies = load_cookies('cookies.txt')
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    download_url = 'https://ibaotu.com/?m=downloadopen&a=open&id={id}&down_type=1&&isSearch=1&so=1'
    pattern = re.compile('sucai/(\d+).html')
    id = re.findall(pattern, url)
    response = requests.get(download_url.format(id=id[0]), headers=headers, cookies=cookies, stream=True)
    if 'https://ibaotu.com/' == response.url:
        print('cookies已过时!')
        return None
    else:
        return response.url

# __name__ == '__main__' and get_url()