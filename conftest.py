import pytest
import requests
from jsonpath import jsonpath

from common.handle_conf import conf
@pytest.fixture(scope='function')
def admin_login():
    para={"username":"admin","password":"macro123"}
    headers=eval(conf.get("env","headers"))
    url=conf.get("env","base_url")+'/admin/login'
    res=requests.request(method="post",url=url,json=para,headers=headers)
    response=res.json()
    token=jsonpath(response,'$..token')[0]
    yield token

