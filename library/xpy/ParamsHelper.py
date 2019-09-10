##
##
from datetime import datetime
import time

__author = "GTMC"
# __format="%Y-%m-%d %H:%M:%S"
__format = "%Y-%m-%d %H:%M:%S"


def appendCreateInfo(o, author=None):
    if not o:
        o = {}
    if not author:
        author = __author
    o["createBy"] = author
    o["createTime"] = datetime.now().strftime(__format)
    return o


def appendUpdateInfo(o, author=None):
    if not o:
        o = {}
    if not author:
        author = __author
    o["updateBy"] = author
    o["updateTime"] = datetime.now().strftime(__format)
    return o


def getTimestamp():
    return str(int(time.time() * 1000));


def getTime():
    return datetime.now().strftime(__format)


def getAuthor():
    return __author


def getImportAuthor():
    return "IMPORT";
