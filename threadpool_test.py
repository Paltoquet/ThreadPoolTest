'''
Created on 2 aout 2016

@author: Sesa432188
'''
from threading import Thread
import Queue
import time

#change threadpool -> threadpool2 or threadpool3
import threadpool2 as threadpool

class ConsumerThread(Thread):
    
    def __init__(self,queue):
        Thread.__init__(self)
        self.queue = queue
        self.pool = threadpool.ThreadPool(4)
        
    def run(self):
        self.pool.start()
        while True:
            val = self.queue.get(block=True)
            self.pool.enqueue(self.read,val)
            #time.sleep(0.2)
            
    def read(self,val):
        print("debut lecture "+ val)
        time.sleep(2)
        print("fin lecture "+ val)


if __name__ == '__main__':
    queue = Queue.Queue()
    consumer = ConsumerThread(queue)
    consumer.start()
    for i in range(0,3):
        queue.put("Tache "+str(i))

    consumer.join()
        
    
        