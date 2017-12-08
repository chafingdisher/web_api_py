# -*- coding: utf-8 -*-
import sys
import time

import requests

from com.lib_pub.MakeRequests import MakeRequests

__author__ = 129
__date__ = 2017 / 11 / 14


class YWApiTestCase(MakeRequests):
    def get_timestamp(self):
        return str(int(time.time() * 1000))

    # def error_message_check(self, response):
    #     if 'errmsg' in response['head'].keys():
    #         print('接口返回异常消息：【%s】' % response['head']['errmsg'], file=sys.stderr)

    def check_normal_response(self, response):
        self.assertEqual(response['head']['errcode'], 0)

    def cellphone_number_check(self, cellphone):
        try:
            int(cellphone)
        except Exception:
            print('手机号必须为数字.', file=sys.stderr)
            self.fail('手机号必须为数字.')
        China_Mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147]
        China_Unicom = [130, 131, 132, 155, 156, 185, 186, 145, 176]
        China_Telecom = [133, 153, 180, 181, 189, 177]

        self.assertEqual(len(cellphone), 11)
        front_three = int(str(cellphone)[:3])
        self.assertIn(front_three, China_Mobile + China_Unicom + China_Telecom)
        print('电话号码校验通过.')
