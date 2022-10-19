import re

def replace_data(data,cls):
    while re.search('#(.+?)#', data):
        res = re.search('#(.+?)#', str(data))
        item = res.group()
        attr = res.group(1)
        value = getattr(cls,attr)
        data = data.replace(item, str(value))
    return data

def find_rex(data):
    res=re.search('#(.+?)#',data)

    return res

#
# if __name__ == '__main__':
#     data=str({"password": "123456","username": "#phone#"})
#
#     res=find_rex(data)
#     print(res)
#



        

#
#
# cases={'case_id': 1, 'interface': 'add', 'title': '添加项目成功', 'method': 'post', 'url': '/admin/register', 'data': '{"logo":"aliquanullaesseinquis","name":"门即流","factoryStatus":50,"brandStory":"ametnisivoluptate","firstLetter":"autenisianim","showStatus":66,"bigPic":"http://dummyimage.com/400x400","sort":91560748}', 'expected': '{"code":200,"message":"操作成功"}', 'result': None}
#
# con=rex.replace_data(str(cases))
# print(con)