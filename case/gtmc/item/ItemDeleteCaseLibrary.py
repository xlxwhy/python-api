from datetime import datetime, timedelta

from library.xpy import JSON
from library.xpy import ParamsHelper

from library.xpy import TestCase
from library.xpy import TestReport
from case import CaseLibrary
import Const

__host = 'http://localhost:8054'
__version = "v1.0"
__path = "/mat/item"


def getAllCases():
    cases = []
    ################################################################################################################
    case = TestCase.init(CaseLibrary.getBaseDataNum(), '创建基础数据')
    TestCase.build(case, method="post", url=getUrl("/mat/item"))
    TestCase.build(case, paramBody={
        "name": "PY-NAME-" + ParamsHelper.getTimestamp(),
        "remark": "PY-REMARK-" + ParamsHelper.getTimestamp(),
        "description": "PY-DESC-" + ParamsHelper.getTimestamp(),
        "createBy": ParamsHelper.getAuthor(),
        "createTime": ParamsHelper.getTime(),
        "updateBy": ParamsHelper.getAuthor(),
        "updateTime": ParamsHelper.getTime(),
    })
    TestCase.build(case, getResult=
    lambda res:
    Const.SUCCESS if
    TestCase.checkStatus(res, 200) and
    int(TestCase.getValue(JSON.decode(res.text), 'body')) > 100000
    else Const.FAIL
                   )
    TestReport.run([case])

    itemId = TestCase.getValue(JSON.decode(case['data']), 'body')
    case['param']['body']['itemId'] = itemId
    entity = case['param']['body']

    ################################################################################################################
    case = TestCase.init(getNum("001"), '删除保养基项')
    TestCase.build(case, method="delete", url=getUrl("/mat/item/" + itemId))
    TestCase.build(case, getResult=
    lambda res:
    Const.SUCCESS if
    TestCase.checkStatus(res, 200) and
    TestCase.getValue(JSON.decode(res.text), 'body')
    else Const.FAIL
                   )
    cases.append(case)
    ################################################################################################################
    case = TestCase.init(getNum("002"), '删除保养基项+删除后查询')
    TestCase.build(case, method="get", url=getUrl("/mat/item/" + itemId))
    TestCase.build(case, getResult=
    lambda res:
    Const.SUCCESS if
    TestCase.checkStatus(res, 200) and
    TestCase.getValue(JSON.decode(res.text), 'body') is None
    else Const.FAIL
                   )
    cases.append(case)
    ################################################################################################################
    return cases


def getUrl(path):
    return __host + '/api/' + __version + path


def getNum(num):
    return CaseLibrary.CASE_GROUP_ITEM_DELETE + num
