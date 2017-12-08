# -*- coding: utf-8 -*-
__author__ = 129
__date__ = 2017 / 11 / 1

import json


# 对数据进行编码
# 转换为 JSON 对象
def encodedJson(obj):
    with open('data.json', 'w') as f:
        encodedjson = json.dump(obj, f)


# 对数据进行解码
# 读取json对象数据
def get_json_value(data, keys):
    """
    :param data:  json字符串或者json对象
    :param keys:  要获取的目标在json串中的key，由根节点到目标节点的key组成的list
    :return: 目标值  或  None
    """
    # with open('data.json', 'r') as f:
    #     data = json.load(f)
    try:
        dataclone = json.load(data)
    except:
        dataclone = data
    for key in keys:
        dataclone = dataclone[key]
    return dataclone
