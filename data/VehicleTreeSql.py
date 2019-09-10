from data.VehicleTree import VEHICLE_TREE, default_brand


def buildDeleteSql(table, field, min, max):
    return "delete  from " + table + " where " + field + ">=" + str(min) + " && " + field + "<=" + str(max) + ";\n"


# 描述:
#################################################################################################
def buildTable(o, table, isFirst):
    db_column_names = ""
    db_column_values = ""
    for column in o.keys():
        db_column_names += ",`" + column + "`";
        db_column_values += ",'" + str(o[column]) + "'";

    DATABASE = ""
    if isFirst:
        DATABASE += "insert into " + table + "(" + db_column_names[1:len(db_column_names)] + ") values \n"
        DATABASE += " (" + db_column_values[1:len(db_column_values)] + ")\n"
    else:
        DATABASE += ",(" + db_column_values[1:len(db_column_values)] + ")\n"
    return DATABASE


def buildTables(tree, needDelete):
    sql_brand = ""
    sql_series = ""
    sql_version = ""
    sql_attribute = ""
    sql_brand += buildTable(default_brand, "veh_veh_brand", len(sql_brand) == 0);
    for skey in tree.keys():
        so = tree[skey]["entity"];
        sql_series += buildTable(so, "veh_veh_series", len(sql_series) == 0);
        for vkey in tree[skey]["versions"].keys():
            vo = tree[skey]["versions"][vkey]["entity"]
            sql_version += buildTable(vo, "veh_veh_version", len(sql_version) == 0);
            for pkey in tree[skey]["versions"][vkey]["properties"].keys():
                po = tree[skey]["versions"][vkey]["properties"][pkey]["entity"]
                sql_attribute += buildTable(po, "veh_veh_attribute", len(sql_attribute) == 0);

    sql = ""
    sql += buildDeleteSql("veh_veh_brand", "brand_id", default_brand["brand_id"], default_brand["brand_id"]) if needDelete else ""
    sql += sql_brand + ";\n";
    sql += buildDeleteSql("veh_veh_series", "series_id", 800000000, 900000000) if needDelete else ""
    sql += sql_series + ";\n";
    sql += buildDeleteSql("veh_veh_version", "version_id", 800000000, 900000000) if needDelete else ""
    sql += sql_version + ";\n";
    sql += buildDeleteSql("veh_veh_attribute", "attr_id", 900000000, 1000000000) if needDelete else ""
    sql += sql_attribute + ";\n";

    return sql;


## 创建表数据
VEHICLE_SQL = buildTables(VEHICLE_TREE, True)
