# -*- coding: utf-8 -*-
from com.yowoo.lib.yowoo_test_url import YwUrl

__author__ = 129
__date__ = 2017 / 11 / 14


class ServerApi():
    '''
        所有对外暴露的、需要执行的用例都必须以  test_  开头
        其他的用例或者方法，不要以  test_  开头
    '''

    def __init__(self):
        global s_base_url
        s_base_url = YwUrl.get_oltest_url()
