from data.VehicleEntity import VEHICLE_ENTITY, VEHICLE_ENTITY_LL, VEHICLE_ENTITY_KMR
from data.VehicleEntity import VEHICLE_SERIES_MAP_VALUE, VEHICLE_SERIES_MAP_NAME
from data.VehicleEntity import VEHICLE_VERSION_MAP_VALUE, VEHICLE_VERSION_MAP_KEY


def getPropertyList(entity):
    result = []
    for series in entity.keys():
        model = entity[series]["model"]
        config = entity[series]["config"]
        mi = 0
        while mi < len(model):
            for group in config.keys():
                for field in config[group].keys():
                    values = config[group][field];
                    result.append({
                        "series": series,
                        "version": model[mi],
                        "group": group,
                        "field": field,
                        "value": values[mi],
                    })
            mi += 1
    return result


## 生成属性列表
VEHICLE_PROPERTIES = getPropertyList(VEHICLE_ENTITY);

## 拆分车型
for p in VEHICLE_PROPERTIES:
    if p['series'] == VEHICLE_ENTITY_LL:
        if p["version"] in ["185T 进取版", "185T 豪华版", "185T 运动版", "185T 科技版", "185T 尊享版"]:
            p['series'] = VEHICLE_SERIES_MAP_VALUE['004036']["name"]
        elif p["version"] in ["双擎进取版", "双擎豪华版", "双擎运动版", "双擎科技版", "双擎尊享版"]:
            p['series'] = VEHICLE_SERIES_MAP_VALUE['004038']["name"]

    elif p['series'] == VEHICLE_ENTITY_KMR:
        if p["version"] in ["2.0E 精英版", "2.0E 领先版", "2.0G 豪华版", "2.5G 豪华版", "2.5Q 旗舰版"]:
            p['series'] = VEHICLE_SERIES_MAP_VALUE['004033']["name"]
        elif p["version"] in ["2.0S 锋尚版", "2.5S 锋尚版"]:
            p['series'] = VEHICLE_SERIES_MAP_VALUE['004034']["name"]
        elif p["version"] in ["2.5HG 豪华版", "2.5HQ 旗舰版", "2.5HS 锋尚版"]:
            p['series'] = VEHICLE_SERIES_MAP_VALUE['004035']["name"]
