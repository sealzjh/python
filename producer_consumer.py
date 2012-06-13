#!/usr/bin/python
from threading import Thread,Condition,currentThread
import time

class Goods:
  def __init__(self):
    self.count = 0
  def produce(self,num=1): #add product
    self.count+=num
  def consume(self):
    if self.count:
      self.count-=1
  def isEmpty(self):
    return not self.count

def Producer(Thread):  #create
  def __init__(self,condition,goods,sleeptime=1):
    Thread.__init__(self)
    self.cond = condition
    self.goods = goods
    self.sleeptime = sleeptime
  def run(self):
    cond = self.cond
    goods - self.goods
    while 1 :
      cond.acquire()
      goods.product()
      print "Goods Count:",goods.count,"Producer thread produced"
      cond.notifyAll()
      cond.release()
      time.sleep(self.sleeptime)

class Contumer(Thread):
  def __init__(self,index,condition,goods,sleeptime=4):
    Thread.__init__(self,name = str(index))
    self.cond = condition
    self.goods = goods
    while 1:
      time.sleep(self.sleeptime)
      cond.acquire()
      while goods.isEmpty():
        cond.wait()
      goods.consume()
      print "Goods Count:",goods.count,"Consumer thread",currentThread().getName(),"consumed"
      cond.release()

goods = Goods()
cond = Condition()
producer = Producer(cond , goods)
producer.start()
producer.join()	#wait
for i in range(5):
  consumer = Contumer(i,cond,goods)
  consumer.start()
  consumer.join
