import json


def encode(v):
    return json.dumps(v, indent=2, separators=(',', ': '), ensure_ascii=False)


def decode(v):
    return json.loads(v)


def printo(v):
    print(encode(v))


def append(o, key, value):
    if not o:
        o = {}
    o[key] = value
    return o


def merge(ha, hb):
    h = {}
    if ha:
        for key in ha:
            h[key] = ha[key]
    if hb:
        for key in hb:
            h[key] = hb[key]
    return h
