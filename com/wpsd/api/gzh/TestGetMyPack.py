# -*- coding: utf-8 -*-
import urllib.request

from com.wpsd import JsonUtil

__author__ = 129
__date__ = 2017 / 11 / 1


def test_get_my_pack():
    url = ''
    content = __get_pack(url)
    __get_bid_point(content)
    __get_prov_list(content)
    __get_business_keys(content)


def __provider_login():
    pass


def __get_pack(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    content = response.read()
    return content


def __get_bid_point(content):
    bid_point_key = ['pack', 'bid_point']
    JsonUtil.get_json_value(content, bid_point_key)


def __get_prov_list(content):
    prov_list_key = ['pack', 'prov_list']
    JsonUtil.get_json_value(content, prov_list_key)


def __get_business_keys(content):
    business_keys = ['business_keys']
    JsonUtil.get_json_value(content, business_keys)
