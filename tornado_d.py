#!/usr/bin/env python
#encoding=utf-8
from daemon import daemon
import os
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler,Application,url
import tornado.httpserver

class HelloHandler(RequestHandler):
    def get(self):
        self.write("hello,world")

class IndexHandler(RequestHandler):
    def get(self,input):
        greeting = self.get_argument('greeting','hi')
        self.write(greeting+',man!!! your No. is '+input)
    def write_error(self,status_code,**kwargs):
        self.write("so sorry!!!you got a %d error"% status_code)
if __name__=="__main__":
    daemonctx = daemon.DaemonContext()
    daemonctx.stdin = open('/dev/null', 'r')
    daemonctx.stdout = open('/dev/null', 'w+')
    daemonctx.stderr = open('/dev/null', 'w+', buffering=0)
    daemonctx.working_directory = os.getcwd()
    daemonctx.umask = 022
    daemonctx.open()
    app=Application([(r"/",HelloHandler),(r"/hi/([0-9]+)",IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    app.listen(8888)
    IOLoop.current().start()
