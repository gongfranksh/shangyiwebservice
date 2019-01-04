#!/usr/bin/python
# coding:utf-8

from spyne import Application, rpc, ServiceBase
from spyne import Integer, Unicode, Array, ComplexModel, Iterable, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from ShangYi.jsMethod import JsService


class Person(ComplexModel):
    name = Unicode
    age = Integer


class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(self, name, times):
        for i in range(times):
            yield "Hello %s, It's the %s time to meet you." % (name, i + 1)

    @rpc(Array(Person), _returns=Iterable(Unicode))
    def say_hello_1(self, persons):
        print('-------say_hello_1()--------')
        if not persons:
            yield 'None'
        for person in persons:
            print('name is : %s, age is %s.' % (person.name, person.age))
            yield 'name is : %s, age is %s.' % (person.name, person.age)


class HelloWorldService2(ServiceBase):
    @rpc(Array(String), _returns=Iterable(Unicode))
    def say_hello_2(self, persons):
        if not persons:
            yield 'None'

        for person in persons:
            yield person



application = Application([HelloWorldService, HelloWorldService2, JsService],
                          'weiliang.shangyi.webservice',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())
wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    import logging
    host = '192.168.81.136'
    port = 8000
    logfilename='shangyiservice.log'
    logging.basicConfig(level=logging.DEBUG, filename=logfilename, format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    logging.getLogger('spyne.application.server').setLevel(logging.DEBUG)
    logging.info("listening to http://%s:%s" % (host,port))
    logging.info("wsdl is at: http://%s:%s/?wsdl" % (host,port) )
    server = make_server(host, port, wsgi_application)
    server.serve_forever()
