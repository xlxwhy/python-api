from datetime import datetime, timedelta

from case import CaseLibrary
from library.xpy import JSON
from library.xpy import ParamsHelper

from library.xpy import TestCase
import Const

__host = 'http://localhost:8054'
__version = "v1.0"
__path = "/mat/item"


def getAllCases():
    cases = []
    ################################################################################################################
    case = TestCase.init(getNum("001"), '创建保养基项')
    TestCase.build(case, method="post", url=getUrl(__path))
    TestCase.build(case, paramBody={
        "name": "PY-NAME-" + ParamsHelper.getTimestamp(),
        "remark": "PY-REMARK-" + ParamsHelper.getTimestamp(),
        "description": "PY-DESC-" + ParamsHelper.getTimestamp(),
        "createBy": ParamsHelper.getAuthor(),
        "createTime": ParamsHelper.getTime(),
        "updateBy": ParamsHelper.getAuthor(),
        "updateTime": ParamsHelper.getTime(),
    })
    TestCase.build(case, getResult=lambda res: Const.SUCCESS if TestCase.checkStatus(res, 200) else Const.FAIL)
    cases.append(case)
    ################################################################################################################
    case = TestCase.init(getNum("002"), '创建保养基项+没有创建时间')
    TestCase.build(case, method="post", url=getUrl(__path))
    TestCase.build(case, paramBody={
        "name": "PY-NAME-" + ParamsHelper.getTimestamp(),
        "remark": "PY-REMARK-" + ParamsHelper.getTimestamp(),
        "description": "PY-DESC-" + ParamsHelper.getTimestamp(),
        "createBy": ParamsHelper.getAuthor(),
        "updateBy": ParamsHelper.getAuthor(),
        "updateTime": ParamsHelper.getTime(),
    })
    TestCase.build(case, getResult=lambda res: Const.SUCCESS if TestCase.checkStatus(res, 200) else Const.FAIL)
    cases.append(case)

    ################################################################################################################
    case = TestCase.init(getNum("003"), '创建保养基项+没有更新时间')
    TestCase.build(case, method="post", url=getUrl(__path))
    TestCase.build(case, paramBody={
        "name": "PY-NAME-" + ParamsHelper.getTimestamp(),
        "remark": "PY-REMARK-" + ParamsHelper.getTimestamp(),
        "description": "PY-DESC-" + ParamsHelper.getTimestamp(),
        "createBy": ParamsHelper.getAuthor(),
        "createTime": ParamsHelper.getTime(),
        "updateBy": ParamsHelper.getAuthor(),
    })
    TestCase.build(case, getResult=lambda res: Const.SUCCESS if TestCase.checkStatus(res, 200) else Const.FAIL)
    cases.append(case)

    ################################################################################################################
    case = TestCase.init(getNum("004"), '创建保养基项+没有更新者/创建者')
    TestCase.build(case, method="post", url=getUrl(__path))
    TestCase.build(case, paramBody={
        "name": "PY-NAME-" + ParamsHelper.getTimestamp(),
        "remark": "PY-REMARK-" + ParamsHelper.getTimestamp(),
        "description": "PY-DESC-" + ParamsHelper.getTimestamp(),
        # "createBy": ParamsHelper.getAuthor(),
        "createTime": ParamsHelper.getTime(),
        # "updateBy": ParamsHelper.getAuthor(),
        "updateTime": ParamsHelper.getTime(),
    })
    TestCase.build(case, getResult=lambda res: Const.SUCCESS if TestCase.checkStatus(res, 200) else Const.FAIL)
    cases.append(case)

    ################################################################################################################
    case = TestCase.init(getNum("005"), '创建保养基项+没有名称')
    TestCase.build(case, method="post", url=getUrl(__path))
    TestCase.build(case, paramBody={
        # "name": "PY-NAME-" + ParamsHelper.getTimestamp(),
        "remark": "PY-REMARK-" + ParamsHelper.getTimestamp(),
        "description": "PY-DESC-" + ParamsHelper.getTimestamp(),
        "createBy": ParamsHelper.getAuthor(),
        "createTime": ParamsHelper.getTime(),
        "updateBy": ParamsHelper.getAuthor(),
        "updateTime": ParamsHelper.getTime(),
    })
    TestCase.build(case, getResult=lambda res: Const.SUCCESS if TestCase.checkNotStatus(res, 200) else Const.FAIL)
    cases.append(case)

    ################################################################################################################
    case = TestCase.init(getNum("006"), '创建保养基项+没有描述')
    TestCase.build(case, method="post", url=getUrl(__path))
    TestCase.build(case, paramBody={
        "name": "PY-NAME-" + ParamsHelper.getTimestamp(),
        "remark": "PY-REMARK-" + ParamsHelper.getTimestamp(),
        # "description": "PY-DESC-" + ParamsHelper.getTimestamp(),
        "createBy": ParamsHelper.getAuthor(),
        "createTime": ParamsHelper.getTime(),
        "updateBy": ParamsHelper.getAuthor(),
        "updateTime": ParamsHelper.getTime(),
    })
    TestCase.build(case, getResult=lambda res: Const.SUCCESS if TestCase.checkStatus(res, 200) else Const.FAIL)
    cases.append(case)

    ################################################################################################################
    case = TestCase.init(getNum("007"), '创建保养基项+没有备注')
    TestCase.build(case, method="post", url=getUrl(__path))
    TestCase.build(case, paramBody={
        "name": "PY-NAME-" + ParamsHelper.getTimestamp(),
        # "remark": "PY-REMARK-" + ParamsHelper.getTimestamp(),
        "description": "PY-DESC-" + ParamsHelper.getTimestamp(),
        "createBy": ParamsHelper.getAuthor(),
        "createTime": ParamsHelper.getTime(),
        "updateBy": ParamsHelper.getAuthor(),
        "updateTime": ParamsHelper.getTime(),
    })
    TestCase.build(case, getResult=lambda res: Const.SUCCESS if TestCase.checkStatus(res, 200) else Const.FAIL)
    cases.append(case)

    ################################################################################################################

    return cases


def getUrl(path):
    return __host + '/api/' + __version + path


def getNum(num):
    return CaseLibrary.CASE_GROUP_ITEM_CREATE + num
