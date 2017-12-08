# -*- coding: utf-8 -*-
from com.yowoo.lib.YWApiTestCase import YWApiTestCase

__author__ = 129
__date__ = 2017 / 11 / 14

from com.yowoo.lib.yowoo_test_url import YwUrl


class OwnerApi(YWApiTestCase):
    '''
        所有对外暴露的、需要执行的用例都必须以  test_  开头
        其他的用例或者方法，不要以  test_  开头
    '''
    def __init__(self):
        global o_base_url
        o_base_url = YwUrl.get_oltest_url()

    def test_owner_release_house(self):
        sufix = '/release-listings'
        url = o_base_url + sufix
        data = {

        }
        # res = requests.post(url=url, data=data)

        pass
