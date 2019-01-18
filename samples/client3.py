# coding:utf-8
import json
import traceback

from zeep import Client

from Entity.SystemFunction import SystemFunction


ip = '192.168.81.136'
port = 8000
client = Client("http://%s:%s/?wsdl" % (ip, port))

factory = client.type_factory("ns0")
try:
    r=client.service.get_functionmenu_all("01002")
# r = client.service.get_productbarcode_all('01002')
# r = client.service.get_productbarcode_by_barcode_result('2000000290645')
# r = client.service.get_productbarcode()

# print type(r)
# print r
except:
    traceback.print_exc()



p= json.loads(r)

print p

# for i in p:
#     # print type(i)
#     # print i
#     print i['ProId']
#     print i['Spec']

