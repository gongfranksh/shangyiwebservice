# coding:utf-8

from suds.client import Client

host = '127.0.0.1'
port = 8000

client = Client('http://%s:%s/?wsdl' % (host, port))
print client

persons = client.service.say_hello('zhangsan', 2)
print persons


print '-' * 20
person = {}
person['name'] = 'zhangsan'
person['age'] = 23

persons = client.factory.create('PersonArray')
persons.Person.append(person)
persons.Person.append(person)
person = client.service.say_hello_1(persons)
print person

print '=' * 20
persons = client.factory.create('stringArray')
persons.string.append('lisi')
persons.string.append('zhangsan')
person = client.service.say_hello_2(persons)
print person

