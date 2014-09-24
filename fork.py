#!/usr/bin/env python
#encoding=utf-8

import os
import time
from multiprocessing import Process,Pool

def func(n,count):
    print '[%d]start run test in child process %s'%(n,os.getpid())
    for i in range(5):
        print '[%s]testing in child process %s'%(n,i)
        time.sleep(2)
    count+=1
    print '[%s]end of the test,count: %d'%(n,count)

if __name__=='__main__':
    count=0
    print 'parent process %s'%os.getpid()
    t1=time.clock()
    p=Pool(5)
    for i in range(5):
        p.apply_async(func,args=(i,count))
    print 'waiting all done'
    p.close()
    p.join()
    t2=time.clock()
    print 'everything is done,used:',t2-t1
    print 'count:',count
