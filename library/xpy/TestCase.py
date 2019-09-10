##
##

from datetime import datetime
import time
from library.xpy import HttpRequest
from library.xpy import JSON
import Const

Const.SUCCESS = 'SUCCESS'
Const.FAIL = 'FAIL'
Const.IGNORE = 'IGNORE'


def build(case=None, num=None, name=None, url=None, method=None, paramBody=None, paramQuery=None, paramPth=None, getResult=None, time=None, data=None, ignore=False):
    case = init() if not case else case
    if num: case['num'] = num
    if name: case['name'] = name
    if url: case['url'] = url
    if method: case['method'] = method
    if paramBody: case['param']['body'] = paramBody
    if paramQuery: case['param']['query'] = paramQuery
    if paramPth: case['param']['path'] = paramPth
    if getResult: case['getResult'] = getResult
    if time: case['time'] = time
    if data: case['data'] = data
    if ignore: case['ignore'] = ignore

    return case


def init(num=None, name=None):
    return {
        "num": num,
        "name": name,
        "url": None,
        "method": None,
        "param": {
            "body": {
                "itemId": None,
                "name": None,
                "remark": None,
                "description": None,
            },
            "query": None,
            "path": None,
        },
        "getResult": None,
        "time": None,
        "ignore": False,
    }


def checkStatus(res, status):
    return True if res.status_code == status else False


def checkNotStatus(res, status):
    return True if res.status_code != status else False


def checkValue(res, status, value=None, fa=None, fb=None, fc=None, fd=None, fe=None, ff=None, fg=None, fh=None, fi=None):
    if not checkStatus(res, status):
        return False
    if not value:
        return True
    if not res.text:
        return False

    data = JSON.decode(res.text)
    v = getValue(data, fa, fb, fc, fd, ff, fg, fh, fi)

    return value == v


def getValue(data, fa=None, fb=None, fc=None, fd=None, fe=None, ff=None, fg=None, fh=None, fi=None):
    v = data
    v = getFieldValue(v, fa) if fa else v
    v = getFieldValue(v, fb) if fb else v
    v = getFieldValue(v, fc) if fc else v
    v = getFieldValue(v, fd) if fd else v
    v = getFieldValue(v, fe) if fe else v
    v = getFieldValue(v, ff) if ff else v
    v = getFieldValue(v, fg) if fg else v
    v = getFieldValue(v, fh) if fh else v
    v = getFieldValue(v, fi) if fi else v
    return v


def getFieldValue(o, key):
    return o[key] if (o and key and key in o.keys()) else None
