# -*- coding: utf-8 -*-
from com.yowoo.lib.YWApiTestCase import YWApiTestCase

from com.yowoo.lib.yowoo_test_url import YwUrl

__author__ = 129
__date__ = 2017 / 11 / 14


class RenterApi(YWApiTestCase):
    '''
    所有对外暴露的、需要执行的用例都必须以  test_  开头
    其他的用例或者方法，不要以  test_  开头
    '''

    def __init__(self):
        self.r_base_url = YwUrl.get_oltest_url()
        self.timestamp = self.get_timestamp()

    def test_fuzzy_query_estate(self):
        url = self.r_base_url + 'estate'
        query_key = '测试'
        data = {
            "name": query_key,
            "t": self.timestamp
        }
        response = self.request('get', url, data)
        self.assertEqual(response['head']['errcode'], 0)
        estates = response['data']
        # 查询到的小区数量
        self.assertGreatThan(len(estates), 0)
        # 小区名称是否包含
        for estate in estates:
            print(estate)
            self.assertIn(query_key, estate['name'])
        '''可以再检验返回数据的其他字段'''

    def test_query_metro_station(self):
        url = self.r_base_url + '/queryStation'
        city_id = '1964522000000185'  # 深圳
        data = {
            "cityId": city_id,
            "t": self.timestamp
        }
        response = self.request('get', url, data)
        self.assertEqual(response['head']['errcode'], 0)
        metro_lines = response['data']
        self.assertGreatThan(len(metro_lines), 0)
        print(metro_lines)
        '''可以再检验返回数据的其他字段'''

    def test_query_building_unit(self):
        url = self.r_base_url + 'queryUnit'
        buildingId = '19704409000029357'  # 测试小区 estateId = 19704408000004286
        data = {
            "buildingId": buildingId,
            "t": self.timestamp
        }
        response = self.request('get', url, data)
        self.assertEqual(response['head']['errcode'], 0)
        self.assertGreatThan(len(response['data']), 0)
        '''可以再检验返回数据的其他字段'''

    def test_query_building_floor(self):
        url = self.r_base_url + 'queryFloor'
        buildingId = '19704409000029357'
        unitName = '一单元'
        data = {
            "buildingId": buildingId,
            "unitName": unitName,
            "t": self.timestamp
        }
        response = self.request('get', url, data)
        self.assertEqual(response['head']['errcode'], 0)
        self.assertGreatThan(response['data'], 0)
        '''可以再检验返回数据的其他字段'''

    def test_query_room_number_1(self):
        url = self.r_base_url + 'queryRoom'
        buildingId = '19704409000029357'
        unitName = '一单元'
        floor = '4'
        data = {
            "buildingId": buildingId,
            "unitName": unitName,
            "floor": floor,
            "t": self.timestamp
        }
        response = self.request('get', url, data)
        self.assertEqual(response['head']['errcode'], 0)
        self.assertEqual(len(response['data']), 0)
        for room in response['data']:
            self.assertIn(''.join([unitName, floor]), room['roomNo'])
        '''可以再检验返回数据的其他字段'''

    def test_query_room_number_2(self):
        url = self.r_base_url + 'queryRoom'
        buildingId = '19704409000029357'
        unitName = '一单元'
        floor = '2'
        data = {
            "buildingId": buildingId,
            "unitName": unitName,
            "floor": floor,
            "t": self.timestamp
        }
        response = self.request('get', url, data)
        self.assertEqual(response['head']['errcode'], 0)
        self.assertGreatThan(len(response['data']), 0)
        for room in response['data']:
            print(room['roomNo'])
            self.assertIn(''.join([unitName, floor]), room['roomNo'])
        '''可以再检验返回数据的其他字段'''

    def test_add_estate_info(self):
        url = self.r_base_url + 'estate/addEstateDemand'
        name = '19704409000029357'
        price = '1234'
        description = '测试'
        data = {
            "name": name,
            "price": price,
            "description": description,
            "t": self.timestamp
        }
        response = self.request('get', url, data)
        self.assertEqual(response['head']['errcode'], 0)

    def test_renter_make_reverse_1(self):
        url = self.r_base_url + '/make'
        json = {
            "renterNumber": None,
            "waiterNumber": None,
            "renterId": 9845685,
            "waiterId": 78458956,
            "estateId": 845656,
            "estateName": 46556,
            "houseId": 8945623,
            "buildingId": 894562130,
            "buildingName": 98465123,
            "roomNo": 8495623,
            "renterMakeTime": 895623,
            "makeSource": 1,
            "remark": None
        }
        response = self.request('post', url=url, json=json)
        self.assertEqual(response['head']['errcode'], 0)
        self.assertEqual('success', response['data'])

    def test_renter_make_reverse_2(self):
        url = self.r_base_url + '/make'
        json = {
            "renterNumber": None,
            "waiterNumber": None,
            "renterId": 9845685,
            "waiterId": 78458956,
            "estateId": 845656,
            "estateName": 46556,
            "houseId": 8945623,
            "buildingId": 894562130,
            "buildingName": 98465123,
            "roomNo": 8495623,
            "renterMakeTime": 895623,
            "makeSource": 2,
            "remark": None
        }
        response = self.request('post', url=url, json=json)
        self.assertEqual(response['head']['errcode'], 0)
        self.assertEqual('success', response['data'])

    def test_renter_make_reverse_3(self):
        url = self.r_base_url + '/make'
        json = {
            "id": 89562,
            "userType": 1,
            "renterId": 9845685,
            "renterMakeTime": None,
            "renterConfirmStatus": 1,
            "waiterMakeTime": None,
            "waiterConfirmStatus": 2,
            "renterNumber": None,
            "makeSource": 3,
            "remark": None
        }
        response = self.request('post', url=url, json=json)
        self.assertEqual(response['head']['errcode'], 0)
        self.assertEqual('success', response['data'])


if __name__ == '__main__':
    rr = RenterApi()
    rr.test_renter_make_reverse_2()
