import os

import pytest
from common.handle_excel import HandleExcel
from common.handle_path import CASE_DIR, DATA_DIR, CONF_DIR
from testcases.base_cases import BaseCase


class TestLogin(BaseCase):
    cases = HandleExcel(os.path.join(DATA_DIR, "cases.xlsx"), "login").read_data()
    name="登陆"

    @pytest.mark.parametrize("case", cases)
    def test_login_success(self, case):
        self.checkout(case)
    def test_login_fail(self):
        pass
    # 断言
