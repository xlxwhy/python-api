import Const

CASE_GROUP_ITEM_CREATE = "C10101"
CASE_GROUP_ITEM_GET = "C10102"
CASE_GROUP_ITEM_DELETE = "C10103"
CASE_GROUP_ITEM_UPDATE = "C10104"

CASE_GROUP_VEHICLE_BASE = "C10200"

CASE_GROUP_BASE = "B00000"

__base_num = 10000000


def getBaseDataNum():
    global __base_num
    __base_num += 1
    return "B" + str(__base_num)
