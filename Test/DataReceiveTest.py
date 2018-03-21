import threading
from time import sleep, ctime

loops = [8,2]


def test() :
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

if  __name__ == '__main__' :

   test()

