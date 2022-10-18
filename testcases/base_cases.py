import os

import requests
from common.handle_conf import conf
from common.handle_log import my_log
# from common import conf


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
        self.url = self.base_url + self.case['url']
        self.method = self.case['method'].lower()
        self.para = eval(self.case['data'])
        self.expeted = eval(self.case['expected'])
        self.headers = eval(conf.get("env", 'headers'))

    def step(self):
        # self.response=requests.request(self.method,self.url,self.para,self.headers)
        # self.result
        self.response = requests.request(method=self.method, url=self.url, json=self.para, headers=self.headers)
        self.log.info(self.response.json())

    #
    # def setup(self):
    #     my_log.info("--------开始执行{}用例---".format(self.name))
    #
    # def teardown(self):
    #
    #     my_log.info("---------执行用例{}结束".format(self.name))
    @classmethod
    def teardown_clss(cls):
        my_log.info("-------------{}结束测试-------".format(cls.name))

    def assert_code(self):
        pass

    def assert_json(self):
        pass

    def assert_sql(self):
        pass
