from data.VehicleProperty import VEHICLE_PROPERTIES, VEHICLE_SERIES_MAP_NAME
from data.VehicleProperty import VEHICLE_VERSION_MAP_VALUE, VEHICLE_VERSION_MAP_KEY
from library.xpy import ParamsHelper, JSON
from data.VehicleLibrary import getKey, getPrice, getAttributeValue, getAttributeGroup


# 800100101
def buildId(sid, vid, mid):
    BASE_ID = 800000000;
    return BASE_ID + sid * 100000 + vid * 100 + mid;


def buildAttributeId(pid):
    BASE_ID = 900000000;
    return BASE_ID + pid;


# 各个表的默认值
##########################################################################################
# buildDefaultBrand
def buildDefaultBrand():
    return {
        "brand_id": "1",
        "pid": "0",
        "name": "广汽丰田",
        "manufacturer_type": "0",
        "logo_path": "",
        "cn_name": "",
        "en_name": "",
        "letter": "",
        "description": "",
        "sort": "1",
        "create_by": ParamsHelper.getImportAuthor(),
        "create_time": ParamsHelper.getTime(),
        "update_by": ParamsHelper.getImportAuthor(),
        "update_time": ParamsHelper.getTime(),
    }


default_brand = buildDefaultBrand();


# buildDefaultSeries
# 导入veh_veh_series表时，需要明确以下字段的默认取值:
# brand_id、bookable、earnest_money、image_path、thumbnail_path、tags、remark、sort、status、delete_flag
def buildDefaultSeries():
    return {
        "series_id": "",
        "name": "",
        "code": "",
        "brand_id": default_brand["brand_id"],
        "bookable": "0",
        "earnest_money": "0",
        "image_path": "",
        "thumbnail_path": "",
        "tags": "",
        "remark": "",
        "sort": '',
        "status": '0',
        "delete_flag": '0',
        "create_by": ParamsHelper.getImportAuthor(),
        "create_time": ParamsHelper.getTime(),
        "update_by": ParamsHelper.getImportAuthor(),
        "update_time": ParamsHelper.getTime(),
    };


# buildDefaultVersion
# 导入veh_veh_version表时，需要明确以下字段的默认取值:
# brand_id、brand_name、main_image_path、subsidized_price、description、sort、delete_flag
def buildDefaultVersion():
    return {
        "version_id": "",
        "version_name": "",
        "version_code": "",
        "brand_id": default_brand["brand_id"],
        "brand_name": default_brand["name"],
        "series_id": "",
        "series_name": "",
        "series_code": "",
        "main_image_path": "0",
        "subsidized_price": "0",
        "guide_price": "",
        "description": "",
        "sort": "",
        "delete_flag": "0",
        "create_by": ParamsHelper.getImportAuthor(),
        "create_time": ParamsHelper.getTime(),
        "update_by": ParamsHelper.getImportAuthor(),
        "update_time": ParamsHelper.getTime(),
    };


# buildDefaultAttribute
# 导入veh_veh_attribute表时，需要明确以下字段的默认取值:
# brand_id
def buildDefaultAttribute():
    return {
        "attr_id": "",
        "brand_id": default_brand["brand_id"],
        "version_id": "",
        "version_code": "",
        "version_name": "",
        "attr_group_name": "",
        "attr_name": "",
        "attr_value": "",
        "create_by": ParamsHelper.getImportAuthor(),
        "create_time": ParamsHelper.getTime(),
        "update_by": ParamsHelper.getImportAuthor(),
        "update_time": ParamsHelper.getTime(),
    };


# 生成基础树结构(仅填充默认值及Property的三个字段: group/field/value)
##########################################################################################
def buildDefaultTree(ps):
    ptree = {};
    for p in ps:
        is_guide_price = p["field"] == "官方指导价";
        if p['series'] not in ptree.keys():
            # 车系结构
            ptree[p["series"]] = {}
            ptree[p["series"]]["versions"] = {}
            ptree[p["series"]]["entity"] = buildDefaultSeries();
        if p["version"] not in ptree[p["series"]]["versions"].keys():
            # 车系版本结构
            ptree[p["series"]]["versions"][p["version"]] = {}
            ptree[p["series"]]["versions"][p["version"]]["properties"] = {}
            ptree[p["series"]]["versions"][p["version"]]["entity"] = buildDefaultVersion()
            if is_guide_price:
                ptree[p["series"]]["versions"][p["version"]]["entity"]["guide_price"] = getPrice(p["value"]);
        if not is_guide_price:
            if p["field"] not in ptree[p["series"]]["versions"][p["version"]]["properties"].keys() and not is_guide_price:
                # 车系版本属性结构
                ptree[p["series"]]["versions"][p["version"]]["properties"][p["field"]] = {}
                ptree[p["series"]]["versions"][p["version"]]["properties"][p["field"]]["entity"] = buildDefaultAttribute()
                # 必须提前填充数据
                ptree[p["series"]]["versions"][p["version"]]["properties"][p["field"]]["entity"]["attr_group_name"] = getAttributeGroup(p["group"])
                ptree[p["series"]]["versions"][p["version"]]["properties"][p["field"]]["entity"]["attr_name"] = p["field"]
                ptree[p["series"]]["versions"][p["version"]]["properties"][p["field"]]["entity"]["attr_value"] = getAttributeValue(p["value"])
            else:
                print("ERROR! duplicate field:[" + p['field'] + "]");
    return ptree;


# 填充数据: 填充ID、CODE、NAME及关联数据
##########################################################################################
def buildTree(tree):
    sid = 0;
    vid = 0;
    mid = 0;
    pid = 0;
    so = {};
    vo = {};
    mo = {};
    for skey in tree.keys():
        sid += 1;
        vid = 0;
        mid = 0;

        so = tree[skey]["entity"];
        so["series_id"] = buildId(sid, vid, mid)
        so["code"] = VEHICLE_SERIES_MAP_NAME[skey]["car_code"];
        so["name"] = VEHICLE_SERIES_MAP_NAME[skey]["name"];
        so["sort"] = VEHICLE_SERIES_MAP_NAME[skey]["sort"];
        for vkey in tree[skey]["versions"].keys():
            vid += 1;
            mid = 0;

            vo = tree[skey]["versions"][vkey]["entity"];
            version_key = getKey(VEHICLE_SERIES_MAP_NAME[skey]["value"] + "-" + vkey)
            vo["version_id"] = buildId(sid, vid, mid)
            vo["version_code"] = VEHICLE_VERSION_MAP_KEY[version_key]["value"];
            vo["version_name"] = VEHICLE_VERSION_MAP_VALUE[vo["version_code"]]["name"];
            vo["series_id"] = so["series_id"];
            vo["series_code"] = so["code"];
            vo["series_name"] = so["name"];
            vo["sort"] = str(vid);

            for pkey in tree[skey]["versions"][vkey]["properties"].keys():
                pid += 1;

                po = tree[skey]["versions"][vkey]["properties"][pkey]["entity"];
                po["attr_id"] = buildAttributeId(pid);
                po["version_id"] = vo["version_id"];
                po["version_code"] = vo["version_code"];
                po["version_name"] = vo["version_name"];

    return tree;


# 创建树结构
VEHICLE_TREE = buildDefaultTree(VEHICLE_PROPERTIES)

# 填充数据
VEHICLE_TREE = buildTree(VEHICLE_TREE)
