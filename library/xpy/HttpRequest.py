##
##
import requests

from library.xpy import JSON

__headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
}

__headers__post = JSON.append(__headers, 'Content-Type', 'application/json')


def post(url, data, headers=None):
    headers = JSON.merge(headers, __headers__post)
    return requests.post(url, JSON.encode(data), headers=headers)


def request(method, url, params, headers=None):
    headers = JSON.merge(headers, __headers__post)
    return requests.request(method, url, data=JSON.encode(params['body']), params=params['query'], headers=headers)
