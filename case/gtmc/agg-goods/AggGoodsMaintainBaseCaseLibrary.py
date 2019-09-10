from datetime import datetime, timedelta

from library.xpy import JSON
from library.xpy import ParamsHelper

from library.xpy import TestCase
from library.xpy import TestReport
from case import CaseLibrary
import Const

__host = 'http://localhost:8050'
__version = "v1.0"


def getUrl(path, pa=None, pb=None, pc=None, pd=None):
    url=__host + '/api/' + __version + path
    url = url + pa if pa else url
    url = url + pb if pb else url
    url = url + pc if pc else url
    url = url + pd if pd else url
    return url


def getNum(num):
    return CaseLibrary.CASE_GROUP_VEHICLE_BASE + num


def getAllCases():
    cases = []
    ignore = False
    ################################################################################################################
    case = TestCase.init(CaseLibrary.getBaseDataNum(), '基础数据+创建车系')
    TestCase.build(case, method="post", url=getUrl("/vehicle/veh-series"))
    TestCase.build(case, paramBody={
        "name": "PY-NAME-" + ParamsHelper.getTimestamp(),
        "code": "PY-CODE-" + ParamsHelper.getTimestamp(),
        "brandId": ParamsHelper.getTimestamp(),
        "imagePath": "PY-IMG-" + ParamsHelper.getTimestamp(),
        "description": "PY-DESC-" + ParamsHelper.getTimestamp(),
        "sort": 1,
        "status": 1,
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
    TestReport.run([case], reportData=False)

    eid = TestCase.getValue(JSON.decode(case['data']), 'body')
    entity = case['param']['body']
    ignore = eid is None


    ################################################################################################################
    entity = {
        "seriesId": eid,
        "name": "PY-NAME-" + ParamsHelper.getTimestamp(),
        "code": "PY-CODE-" + ParamsHelper.getTimestamp(),
        "brandId": ParamsHelper.getTimestamp(),
        "imagePath": "PY-IMG-" + ParamsHelper.getTimestamp(),
        "description": "PY-DESC-" + ParamsHelper.getTimestamp(),
        "sort": 2,
        "status": 2,
        "createBy": "PY-CBY-" + ParamsHelper.getTimestamp(),
        "createTime": ParamsHelper.getTime(),
        "updateBy": "PY-UBY-" + ParamsHelper.getTimestamp(),
        "updateTime": ParamsHelper.getTime(),
    }

    case = TestCase.init(getNum("001"), '修改车系')
    TestCase.build(case, method="post", url=getUrl("/vehicle/veh-series"))
    TestCase.build(case, paramBody=entity)
    TestCase.build(case, ignore=ignore)
    TestCase.build(case, getResult=
    lambda res:
    Const.SUCCESS if
    TestCase.checkStatus(res, 200) and
    TestCase.getValue(JSON.decode(res.text), 'body')
    else Const.FAIL
                   )
    cases.append(case)
    ################################################################################################################

    case = TestCase.init(getNum("002"), '修改车系+修改后检查所有字段是否正确')
    TestCase.build(case, method="get", url=getUrl("/vehicle/veh-series/", eid))
    TestCase.build(case, ignore=ignore)
    TestCase.build(case, getResult=
    lambda res:
    Const.SUCCESS if
    TestCase.checkStatus(res, 200) and
    TestCase.getValue(JSON.decode(res.text), 'body', 'updateBy') == entity['createBy'] and
    TestCase.getValue(JSON.decode(res.text), 'body', 'updateTime') == entity['createTime'] and
    TestCase.getValue(JSON.decode(res.text), 'body', 'createBy') == entity['createBy'] and
    TestCase.getValue(JSON.decode(res.text), 'body', 'createTime') == entity['createTime'] and
    TestCase.getValue(JSON.decode(res.text), 'body', 'status') == entity['status'] and
    TestCase.getValue(JSON.decode(res.text), 'body', 'sort') == entity['sort'] and
    TestCase.getValue(JSON.decode(res.text), 'body', 'description') == entity['description'] and
    TestCase.getValue(JSON.decode(res.text), 'body', 'imagePath') == entity['imagePath'] and
    TestCase.getValue(JSON.decode(res.text), 'body', 'brandId') == entity['brandId'] and
    TestCase.getValue(JSON.decode(res.text), 'body', 'code') == entity['code'] and
    TestCase.getValue(JSON.decode(res.text), 'body', 'name') == entity['name'] and
    TestCase.getValue(JSON.decode(res.text), 'body', 'seriesId') == entity['seriesId']
    else Const.FAIL
                   )
    cases.append(case)

    ################################################################################################################
    case = TestCase.init(getNum("003"), '修改车系+清除测试数据')
    TestCase.build(case, method="delete", url=getUrl("/vehicle/veh-series/", eid))
    TestCase.build(case, ignore=ignore)
    TestCase.build(case, getResult=
    lambda res:
    Const.SUCCESS if
    TestCase.checkStatus(res, 200) and
    TestCase.getValue(JSON.decode(res.text), 'body')
    else Const.FAIL
                   )
    cases.append(case)
    ################################################################################################################
    return cases
