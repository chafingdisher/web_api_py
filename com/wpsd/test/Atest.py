# -*- coding: utf-8 -*-
import os

from com.wpsd.util import JsonUtil

__author__ = 129
__date__ = 2017 / 10 / 31

import json
def aaa():
    data = {"pack": {"bid_point": 40, "accum_bid_point": 4, "prov_list": ["湖南省", "广东省"]}}
    list = ['pack', 'bid_point']
    # with open('data.json', 'w') as f:
    #     json.dump(data, f)
    with open('data.json', 'r') as f:
        data = json.load(f)
        value = JsonUtil.get_json_value(data, list)
        print(value)
        # decodeJson(data, list)
        # liststr =  '[\''+'\'][\''.join(list)+'\']'
        # print(liststr)


def decodeJson(data, keys):
    # with open('data.json', 'r') as f:
    #     data = json.load(f)

    # data = json.loads(encodedjson)
    keylist = '[\'' + '\'][\''.join(keys) + '\']'
    print(keylist)
    dataclone = data
    for key in keys:
        dataclone = dataclone[key]
        print(dataclone)
    # print(data['pack']['bid_point'])


def check_num(num):
    try:
        int(num)
    except:
        print('22222222222')
    China_Mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 17]
    China_Unicom = [130, 131, 132, 155, 156, 185, 186, 145, 176]
    China_Telecom = [133, 153, 180, 181, 189, 177]

    three = str(num)[:3]
    print(three)
    if 138 in China_Telecom + China_Unicom + China_Mobile:
        print('3333333333333333')
    else:
        print('rrrrrrrrrrrr')

def get_path():
    work_dir = os.path.dirname(os.path.abspath(__file__))
    print(work_dir)

if __name__ == "__main__":
    get_path()