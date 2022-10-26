import pymysql

coon=pymysql.connect(host="192.168.3.132",database="mall",port=3306,user="reader",password="123456")
# print(coon)
cur=coon.cursor()
sql="select * from pms_product "
res =cur.execute(sql)
# res.__dict__
# all=res.fetchall()
res=cur.fetchall()
print(res)

cur.close()
coon.close()