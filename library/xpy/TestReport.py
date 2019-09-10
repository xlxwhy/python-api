##
##

import time
import Const
from library.xpy import HttpRequest


def printCase(r):
    v = "{!s} [{!s}] {!s} {!s} {!s} {!s}"
    v = v.format(fix(r["num"], 10), fix(r["method"], 6), fix(r["url"], 80), fix(r["status"], 10), fix(r["time"], 10), r["name"])
    print(v)


def fix(v, fixLen):
    v = str(v)
    vlen = len(v)
    if fixLen > vlen:
        return v + (' ' * (fixLen - vlen))
    else:
        return v


def report(r):
    printCase(r)


def reports(rs):
    for r in rs:
        printCase(r)


def run(cases, needReport=True, reportData=False, needTotal=False):
    total = 0
    failTotal = 0
    successTotal = 0
    ignoreTotal=0
    for case in cases:
        if case["ignore"]:
            case['status'] = Const.IGNORE
            case['time'] = "-"
            case['data'] = ""
        else:
            stime = int(time.time() * 1000)
            res = HttpRequest.request(case["method"], case["url"], case['param'])
            etime = int(time.time() * 1000)
            case['status'] = case['getResult'](res)
            case['time'] = str(etime - stime) + "ms"
            case['data'] = res.text
        if needReport:
            report(case)
            if reportData:
                print((case['data']))
        total += 1
        failTotal += 1 if case['status'] == Const.FAIL else 0
        successTotal += 1 if case['status'] == Const.SUCCESS else 0
        ignoreTotal += 1 if case['status'] == Const.IGNORE else 0
    if needTotal:
        print("Total:{!s}  Fail:{!s}  Success:{!s} Ignore:{!s}".format(total, failTotal, successTotal, ignoreTotal))

    return cases
