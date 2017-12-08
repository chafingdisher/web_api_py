# -*- coding: utf-8 -*-
from com.yowoo.lib.YWApiTestCase import YWApiTestCase

__author__ = 129
__date__ = 2017 / 11 / 14

from com.yowoo.lib.yowoo_test_url import YwUrl


class WaiterApi(YWApiTestCase):
    '''
        所有对外暴露的、需要执行的用例都必须以  test_  开头
        其他的用例或者方法，不要以  test_  开头
    '''
    def __init__(self):
        self.w_base_url = YwUrl.get_oltest_url()
        self.timestamp = self.get_timestamp()

    def test_waiter_release_house(self):
        sufix = '/release-listings'
        url = self.w_base_url + sufix
        pass

    def test_get_waiter_reservation_list(self):
        url = self.w_base_url + '/make'
        waiter_id = ['15695862000000018']

        for wid in waiter_id:
            date = {
                'userId': wid,
                "userType": 2,
                "t": self.timestamp
            }
            response = self.request('get', url=url, data=date)
            self.assertEqual(response['head']['errcode'], 0)
            lists = response['data']
            for r in lists:
                self.assertNotNoneOrNotEmpty(r['renterNumber'])
                self.assertNotNoneOrNotEmpty(r['waiterNumber'])
                self.assertNotNoneOrNotEmpty(r['estateName'])
                self.assertNotNoneOrNotEmpty(r['buildingName'])
                self.assertNotNoneOrNotEmpty(r['roomNo'])
                self.assertNotNoneOrNotEmpty(r['house']['name'])
                self.assertNotNoneOrNotEmpty(r['building']['name'])
                self.assertNotNoneOrNotEmpty(r['user']['name'])

                self.assertEqual(r['renterId'], r['user']['id'])
                self.assertEqual(r['houseId'], r['house']['id'])

    def test_get_virtual_numbet(self):
        '''
        -- w 15609268000000000 15768026000000144 15695862000000018
        -- r 4134043000000033 4200344000000105 4203561000000115
        -- h 2011909000911926 2011909000911459 2011909000911444
        '''
        postdata = {
            "renterNumber": None,  # 租客电话为空就好
            "waiterNumber": None,  # 管家电话为空就好
            "renterId": 4134043000000033,  # 租客id
            "waiterId": 15609268000000000,  # 管家id
            "estateId": 2011855000001341,  # 小区id
            "estateName": "雅苑",  # 小区名称
            "houseId": 2011909000911926,  # 房屋id
            "buildingId": 2011858000029749,  # 楼栋id
            "buildingName": "B栋",  # 楼栋名称
            "roomNo": "一单元B0509",  # 门牌号
            "makeSource": 1  # 预约单来源 电话预约为1，直接预约为2
        }
        url = self.w_base_url + '/virtual'
        response = self.request('post', url=url, json=postdata)
        self.assertEqual(response['head']['errcode'], 0)
        self.cellphone_number_check(response['data'])

    def test_waiter_feedback(self):
        url = self.w_base_url + '/feedBack'
        json = {
            "makeLookHouseId": 1234,
            "userId": 1569865,
            "houseId": 6548645,
            "userType": 1,
            "houseFeedback": "qwertoyupijhgfldks",
            "houseRemark": "wertyuijhgfb",
            "serviceFeedback": "qwefghjwedf"
        }
        response = self.request('post', url=url, json=json)
        self.assertNotEqual(response['head']['errcode'], 0)
        print(response['data'])


if __name__ == '__main__':
    www = WaiterApi()
    www.test_get_virtual_numbet()
    # www.test_get_waiter_reservation_list()
    www.test_waiter_feedback()
