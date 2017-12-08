# -*- coding: utf-8 -*-
__author__ = 129
__date__ = 2017 / 11 / 2

import urllib.request


def http_get(url):
    resp = urllib.request.urlopen(url)
    print('status code:\t', resp.getcode())
    print('status message:\t', resp.msg)
    print('page header:\t', resp.headers)
    print('page content:\t', resp.read())
    print('content:\t',resp.read())


def http_post(url, data):
    resp = urllib.request.urlopen(url=url, data=data)

if __name__ == '__main__':
    http_get('http://item.jd.com/5811182.html')