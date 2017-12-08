# -*- coding: utf-8 -*-
import time

from com.lib_pub.MakeRequests import MakeRequests

__author__ = 129
__date__ = 2017 / 11 / 29


class WphApiTestCase(MakeRequests):


    def get_timestamp(self):
        return str(int(time.time() * 1000))

    def check_normal_response(self, response):
        # self.error_message_check(response)
        self.assertEqual(response['status'], 200)
