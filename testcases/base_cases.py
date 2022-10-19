import os
import re

import requests
from common.handle_conf import conf
from common.handle_log import my_log
from common.handle_rex import replace_data,find_rex
from common.handle_random_phone import get_phone_num
from jsonpath import jsonpath

class BaseCase():
    name = "base用例"
    log = my_log
    conf = conf
    base_url = conf.get("env", "base_url")

    @classmethod
    def setup_class(cls):
        cls.log.info("---------【{}】模块开始测试------------".format(cls.name))

    def teardown_class(cls):
        cls.log.info(("---------【{}】模块结束测试------------".format(cls.name)))

    def checkout(self, case):
        # 记录xx用例开始执行
        self.log.info("用例【{}】开始测试".format(case['title']))
        self.case = case
        # 处理case数据

        self.pre_test_data()
        # 执行测试
        self.step()
        # 执行响应断言
        self.assert_code()
        # 执行json断言
        self.assert_json()
        # 执行sql校验
        self.assert_sql()

        self.log.info("用例【{}】结束测试".format(case['title']))

    def pre_test_data(self):
        self.phone=get_phone_num()
        if find_rex(self.case['data']) is not None:
            self.para=eval(replace_data(self.case['data'],BaseCase))
        else:
            # self.case=self.case
            self.para = eval(self.case['data'])
        self.url = self.base_url + self.case['url']
        self.method = self.case['method'].lower()
        self.expeted = eval(self.case['expected'])
        try:
            if self.token is not None:
                self.headers=eval(conf.get("env", 'headers'))
                self.headers['Authorization']='Bearer '+self.token
        except AttributeError as e:
            self.headers = eval(conf.get("env", 'headers'))

        # self.headers = eval(headers)


    def step(self):
        # self.response=requests.request(self.method,self.url,self.para,self.headers)
        # self.result
        try:
            # self.log.info(self.para)
            self.response = requests.request(method=self.method, url=self.url, json=self.para, headers=self.headers)
            self.log.info(self.para)
            self.log.info(self.response.json())
        except Exception as e:
            self.log.error(e)
            raise e

    @classmethod
    def teardown_clss(cls):
        my_log.info("-------------{}结束测试-------".format(cls.name))

    def assert_code(self):
        pass
        assert self.response.status_code==200

    def assert_json(self):
        pass

    def assert_sql(self):
        pass

    # def admin_login(self):
    #     para = {"username": "admin", "password": "macro123"}
    #     headers = eval(conf.get("env", "headers"))
    #     url = conf.get("env", "base_url") + '/admin/login'
    #     res = requests.request(method="post", url=url, json=para, headers=headers)
    #     response = res.json()
    #     token = jsonpath(response, '$..token')[0]
    #     return token
    #
