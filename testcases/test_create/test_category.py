import os

import pytest
from common.handle_excel import HandleExcel
from common.handle_path import CASE_DIR, DATA_DIR, CONF_DIR
from testcases.base_cases import BaseCase


class TestAdd(BaseCase):
    cases = HandleExcel(os.path.join(DATA_DIR, "cases.xlsx"), "category").read_data()
    name="添加商品"

    @pytest.mark.parametrize("case", cases)
    def test_create(self, case,admin_login):
        self.token=admin_login
        # setattr('token',admin_login)
        self.checkout(case)
    def test_pms(self):
        pass
    # 断言

