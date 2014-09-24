#!/usr/bin/env python
#encoding=utf-8

import time, threading

def loop():
    print 'thread %s is running' %threading.current_thread().ident
    for i in range(5):
        print 'thread %s>>> %s '%(threading.current_thread(),i)
        time.sleep(5)
    print 'thread %s is done' %threading.current_thread() 

print 'thread %s is running...' % threading.current_thread().ident
t = threading.Thread(target=loop)
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
