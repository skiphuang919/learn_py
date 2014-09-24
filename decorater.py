#!/user/bin/env python
#encoding=utf-8

import time

def timeit(func):
    def wrapper(i):
        start = time.clock()
        func(i)
        end = time.clock()
        print 'used:',end-start
    return wrapper


@timeit
def f(i=101):
    n=0
    I=int(i)
    for x in range(0,I):
        n=n+x
    print 'the result is:',n

if __name__ == "__main__":
    i=raw_input("enter the number:")
    f(i)

