import os

import pytest
from common.handle_excel import HandleExcel
from common.handle_path import CASE_DIR, DATA_DIR, CONF_DIR
from testcases.base_cases import BaseCase


class TestRegister(BaseCase):
    cases = HandleExcel(os.path.join(DATA_DIR, "cases.xlsx"), "register").read_data()
    name="注册"

    @pytest.mark.parametrize("case", cases)
    def test_register_success(self, case):
        self.checkout(case)

