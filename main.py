from library.xpy import TestReport
from case.gtmc.item import ItemDeleteCaseLibrary, ItemUpdateCaseLibrary, ItemGetCaseLibrary, ItemCreateCaseLibrary
from case.gtmc.vehicle import VehicleBaseCaseLibrary

host = 'http://192.168.0.131:8054'
url = host + '/api/v1.0'
url_item = url + '/mat/item'

##########################################################################
# 测试: ItemApi.create()
##########################################################################

title = {
    "num": "No.",
    "method": "method",
    "url": "URL",
    "status": "Status",
    "time": "Time",
    "name": "Case Description",
    "data": "Response",
}

TestReport.report(title)
cases = []
# cases.extend(ItemCreateCaseLibrary.getAllCases())
# cases.extend(ItemGetCaseLibrary.getAllCases())
# cases.extend(ItemDeleteCaseLibrary.getAllCases())
# cases.extend(ItemUpdateCaseLibrary.getAllCases())
cases.extend(VehicleBaseCaseLibrary.getAllCases())

TestReport.report(title)
TestReport.run(cases, needReport=True, reportData=False, needTotal=True)
