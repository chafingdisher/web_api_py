# -*- coding: utf-8 -*-
import inspect
import sys
import traceback
from time import sleep

from com.yowoo.api.ownerapi import OwnerApi
from com.yowoo.api.renterapi import RenterApi
from com.yowoo.api.serverapi import ServerApi

from com.yowoo.api.waiterapi import WaiterApi

__author__ = 129
__date__ = 2017 / 11 / 14


def start_all_api_test():
    renter = RenterApi()
    call_member_test_method(renter)
    waiter = WaiterApi()
    call_member_test_method(waiter)
    owner = OwnerApi()
    call_member_test_method(owner)
    server = ServerApi()
    call_member_test_method(server)


def call_member_test_method(obj):
    methods = [i for i in dir(obj) if inspect.getmembers(obj) and i.startswith('test_')]
    for index, value in enumerate(methods):
        try:
            invoke_case_method(obj, index, value)
        except:
            exception_handler(value)
            # 可以在这里记录失败用例
        print('-' * 85)
        sys.stdout.flush()


def invoke_case_method(obj_instance, index, method_name):
    print()
    print('<' * 30, '开始执行第', index + 1, '个用例', '>' * 30)
    print('-' * 30, '方法名称：', method_name, '-' * 20)
    method = getattr(obj_instance, method_name)
    method()
    print('execute test case【%s】successful' % method_name)


def exception_handler(method_name):
    print('=' * 30, 'exception stack trace', '=' * 30)
    sleep(0.3)
    # 打印异常堆栈
    traceback.print_exc(file=sys.stderr)
    sleep(0.3)
    print('=' * 30, 'exception stack trace', '=' * 30)
    sleep(0.3)
    print('execute test case【%s】failed' % method_name, file=sys.stderr)


if __name__ == '__main__':
    start_all_api_test()
