# -*- coding: utf-8 -*-
import requests
import sys

from com.lib_pub.TestCase import TestCase

__author__ = 129
__date__ = 2017 / 11 / 16


class MakeRequests(TestCase):
    def __result_check(self, response):
        # 返回结果
        # print('http请求返回状态值：【%s】' % response.status_code)
        # print('Request URL:\t', response.url)
        res = response.json()
        # self.error_message_check(res)
        return res

    @classmethod
    def request(cls, method: str, url, data=None, json=None, **kwargs):
        if 'get' == method.lower():
            return cls.__request_get(url=url, data=data, **kwargs)
        elif 'post' == method.lower():
            return cls.__request_post(url=url, data=data, json=json, **kwargs)
        else:
            raise Exception('Unknown method {}'.format(method))

    @staticmethod
    def __request_get(url, data, **kwargs):
        response = requests.get(url=url, params=data, **kwargs)
        return response.json()

    @staticmethod
    def __request_post(url, data=None, json=None, **kwargs):
        response = requests.post(url=url, data=data, json=json, **kwargs)
        return response.json()

    # def error_message_check(self, response):
    #     if 'errmsg' in response['head'].keys():
    #         print('接口返回异常消息：【%s】' % response['head']['errmsg'], file=sys.stderr)