import pytest
import allure_pytest
if __name__ == '__main__':
    pytest.main(['-s', '-q', '--clean-alluredir', '--alluredir=allure-results'])
    # os.system(r"allure generate -c -o allure-report")