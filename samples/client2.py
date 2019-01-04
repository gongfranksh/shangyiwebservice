# coding:utf-8
import json

from zeep import Client

ip = '192.168.81.136'
port = 8000
client = Client("http://%s:%s/?wsdl" % (ip, port))

factory = client.type_factory("ns0")
r = client.service.get_branch_result('01002')
# print type(r)
# print r

p= json.loads(r)

for i in p:
    # print type(i)
    # print i
    print i['BraId']
    print i['BraSName']


# print type(p)
# print p



# print(client.wsdl.dump())

# ### say_hello
# factory = client.type_factory("ns0")
# r = client.service.say_hello('zhansgan', 3)
# print(r)
#
# ### say_hello_1
# factory = client.type_factory("ns0")
# person = factory.Person(name='zhangsan', age=23)
# persons = factory.PersonArray([person, person])
# r = client.service.say_hello_1(persons)
# print(r)
#
#
# ### say_hello_2
# factory = client.type_factory("ns0")
# persons = factory.stringArray(["zhansgan", "lisi"])
# r = client.service.say_hello_2(persons)
# print(r)

