def getKey(value):
    if value is None: return value
    value = value.replace(" ", "");
    value = value.replace("　", "");
    value = value.replace("（", "(");
    value = value.replace("）", ")");
    return value


def getPrice(value):
    if value is None: return 0
    value = value.replace(" ", "");
    value = value.replace("　", "");
    value = value.replace("（", "(");
    value = value.replace("）", ")");
    value = value.replace("万", "");
    value = value.replace("元", "");
    value = str(int(float(value) * 10000))
    return value


def getAttributeValue(value):
    if value is None: return ""
    # value = value.replace("●", "1");
    # value = value.replace("－", "2");
    # value = value.replace("○", "3");
    return value


def getAttributeGroup(value):
    if value is None: return ""
    value = value.replace("■", "");
    return value
