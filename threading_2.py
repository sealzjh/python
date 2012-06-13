#!/usr/bin/python
import threading
import time

class Counter:
  def __init__(self):
    self.value = 0
    self.lock = thread.allocate_lock()
  def increment(self):
    self.lock.acquire()	#get lock
    self.vale = self.value + 1
    value = self.value
    self.lock.release()	#free lock
    return value



class ThreadDemo(threading.Thread):
  def __init__(self,index,create_time , counter):
    threading.Thread.__init__(self)
    self.index = index
    self.create_time = create_time
    self.counter = counter
  def run(self):
    time.sleep(1)
    value = self.counter.increment()
    print(time.time()-self.create_time),"\t",self.index,"\tvalue:",value

counter = Counter()
for index in range(100):
  thread = ThreadDemo(index , time.time() , counter)
  thread.start()
