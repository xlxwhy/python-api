from data.VehicleData import VEHICLE_DATA_VERSION, VEHICLE_DATA_SERIES
from data.VehicleEntity import VEHICLE_VERSION_MAP_KEY, VEHICLE_VERSION_MAP_VALUE, VEHICLE_SERIES_MAP_NAME, VEHICLE_SERIES_MAP_VALUE
from data.VehicleTreeSql import VEHICLE_SQL
from data.VehicleTree import VEHICLE_TREE

from data.VehicleLibrary import getKey


def writeFile(path, content):
    with open(path, 'w+', encoding='utf-8') as f:
        f.write(content)
        f.close()
    return 'DONE';


path = "./import-vehicle.sql";
content = VEHICLE_SQL;
writeFile(path, content);

# 官网数据
###############################################################################
print("官网数据:".format())
print("\t车系总共{!s}个".format(len(VEHICLE_DATA_SERIES)))
print("\t车系版本总共{!s}个".format(len(VEHICLE_DATA_VERSION)))

# 导入数据
###############################################################################
data_import = {
    "total_series": 0,
    "total_version": 0,
    "total_attribute": 0,
    "missing_series_output": 0,
    "missing_series_input": 0,
}


def line():
    print("------------------------------------------------------")


def analyse(tree):
    line()
    # total
    for skey in tree.keys():
        data_import["total_series"] += 1;
        for vkey in tree[skey]["versions"].keys():
            data_import["total_version"] += 1;
            for pkey in tree[skey]["versions"][vkey]["properties"].keys():
                data_import["total_attribute"] += 1;

    # 官网车系文件中，多出来的数据
    for series in VEHICLE_DATA_SERIES:
        if not findCode(tree, 1, series["car_code"]):
            print("\t缺失配置数据的车系: {!s} {!s}".format(series["name"], series["value"]))

    # 官网版本文件中，多出来的数据
    for version in VEHICLE_DATA_VERSION:
        if not findCode(tree, 2, version["value"]):
            print("\t缺失配置数据的版本: {!s} {!s}".format(version["name"], version["value"]))

    # 找不到车系的版本
    for version in VEHICLE_DATA_VERSION:
        if version['parent'] not in VEHICLE_SERIES_MAP_VALUE.keys():
            print("\t没有车系的版本: {!s} {!s}".format(version["name"], version["value"]))

    line()
    return;


def findName(tree, type, value):
    for skey in tree.keys():
        if type == 1 and getKey(value) == getKey(skey): return True;
        for vkey in tree[skey]["versions"].keys():
            if type == 2 and getKey(value) == getKey(vkey): return True;
            for pkey in tree[skey]["versions"][vkey]["properties"].keys():
                if type == 3 and getKey(value) == getKey(pkey): return True;

    return False;


def findCode(tree, type, value):
    for skey in tree.keys():
        so = tree[skey]["entity"]
        if type == 1 and getKey(value) == getKey(so['code']): return True;
        for vkey in tree[skey]["versions"].keys():
            vo = tree[skey]["versions"][vkey]["entity"]
            if type == 2 and getKey(value) == getKey(vo['version_code']): return True;

    return False;


analyse(VEHICLE_TREE);

print("需要导入的数据:".format())
print("\t车品牌总共1个".format())
print("\t车系总共{!s}个".format(data_import["total_series"]))
print("\t车系版本总共{!s}个".format(data_import["total_version"]))
print("\t车系版本属性总共{!s}个".format(data_import["total_attribute"]))
