# -*- coding: utf-8 -*-
from time import sleep

from com.wpsd import BaseDriver

__author__ = 129
__date__ = 2017 / 11 / 9


class JDMS(BaseDriver):
    def __init__(self):
        BaseDriver.__init__(self)

    def test(self):
        self.star_browser('https://miaosha.jd.com/')
        if self.driver is None:
            print('exception happened while opening browser.')
            return
        print(self.driver)
        sleep(35)
        self.stop_browser()


if __name__ == '__main__':
    jdms = JDMS()
    jdms.test()
