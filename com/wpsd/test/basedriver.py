# -*- coding: utf-8 -*-
import inspect

__author__ = 129
__date__ = 2017 / 11 / 9

from Selenium2Library import Selenium2Library
from time import sleep


class BaseDriver(Selenium2Library):

    def __init__(self):
        Selenium2Library.__init__(self)
        self.driver = None

    def star_browser(self, url):
        try:
            print('opening browser with url:', url)
            self.driver = self.open_browser(url, "chrome")
            self.maximize_browser_window()
        except Exception as ex:
            print("open browser fail.\r\n", ex)
        return self.driver

    def stop_browser(self):
        print('closing browser...')
        self.close_browser()

if __name__ == '__main__':
    base = BaseDriver()
    base.star_browser('https://miaosha.jd.com/')
    sleep(5)
    base.stop_browser()
