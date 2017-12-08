# -*- coding: utf-8 -*-
from com.wpsd.WphApiTestCase import WphApiTestCase

__author__ = 129
__date__ = 2017 / 11 / 29

import requests


class OpcApi(WphApiTestCase):
    def __init__(self):
        self.__current_page = 1

    def check_duplicate_supplier(self):
        supplier_list_url = '1234567'
        json_data = {'cate': 1, 'city_id': 440300, 'current_page': self.__current_page}
        user_ids = []
        while True:
            json_data['current_page'] = self.__current_page
            response = self.request('post', supplier_list_url, json=json_data)
            self.check_normal_response(response)
            user_list = response['user_list']
            if len(user_list) == 0:
                break
            user_ids.extend([each['id'] for each in user_list])
            self.__current_page += 1
        self.assertEqual(len(user_ids), len(list(set(user_ids))))


if __name__ == '__main__':
    opc = OpcApi()
    opc.check_duplicate_supplier()
