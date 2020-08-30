from pythonds.basic import Queue


#Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list.

class QueueWithRearAtEndOfList(Queue):

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

qr = QueueWithRearAtEndOfList()
q = Queue()

import timeit
from timeit import Timer
from random import randint as randint


dotimes = 10000
  
 # enqueue testing 
t1x = timeit.Timer('q.enqueue(4)', "from __main__ import q").timeit(number=dotimes)
print("q.enqueue : %d times %10.3f" %(dotimes,t1x))
t2y = timeit.Timer('qr.enqueue(4)', "from __main__ import qr").timeit(number=dotimes)
print("qr.enqueue: %d times %10.3f" %(dotimes,t2y))
t1x = timeit.Timer('q.enqueue(4)', "from __main__ import q").timeit(number=dotimes*10)
print("q.enqueue : %d times %10.2f" %(dotimes*10,t1x))
t2y = timeit.Timer('qr.enqueue(4)', "from __main__ import qr").timeit(number=dotimes*10)
print("qr.enqueue: %d times %10.2f" %(dotimes*10,t2y))

for x in range(dotimes * 10):
      qr.enqueue(4)
      q.enqueue(4)

t1x = timeit.Timer('q.dequeue()', "from __main__ import q").timeit(number=dotimes)
print("q.dequeue : %d times %10.3f" %(dotimes,t1x))
t2y = timeit.Timer('qr.dequeue()', "from __main__ import qr").timeit(number=dotimes)
print("qr.dequeue: %d times %10.3f" %(dotimes,t2y))
t1x = timeit.Timer('q.dequeue()', "from __main__ import q").timeit(number=dotimes*10)
print("q.dequeue : %d times %10.3f" %(dotimes*10,t1x))
t2y = timeit.Timer('qr.dequeue()', "from __main__ import qr").timeit(number=dotimes*10)
print("qr.dequeue: %d times %10.3f" %(dotimes*10,t2y))



#t3z = timeit.Timer('z[100] = 4', "from __main__ import q").timeit(number=dotimes)
#print("dictSize : %d , timetoset %10.15f" %(size3, t3z))
#t4za = timeit.Timer('z[100] = 4', "from __main__ import q").timeit(number=dotimes)
#print("dictSize : %d , timetoset %10.15f" %(size3, t4za))

# ideally you would combine the enque of the qr and the deque of the q
#
class QueueBestOfBothWorlds(Queue):
    def __init__(self):
        self.items = []
        self.getFromIndex = 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.getFromIndex +=1
        # would want to do some sort of clean up to clear all the dead previous indices from memory
        return self.items[self.getFromIndex-1]

qb = QueueBestOfBothWorlds()
qr = QueueWithRearAtEndOfList()
q = Queue()
for x in range(dotimes * 10):
      qr.enqueue(4)
      q.enqueue(4)
      qb.enqueue(4)

 # enqueue testing 
t1x = timeit.Timer('q.enqueue(4)', "from __main__ import q").timeit(number=dotimes)
print("q.enqueue : %d times %10.3f" %(dotimes,t1x))
t2y = timeit.Timer('qr.enqueue(4)', "from __main__ import qr").timeit(number=dotimes)
print("qr.enqueue: %d times %10.3f" %(dotimes,t2y))
t1x = timeit.Timer('q.enqueue(4)', "from __main__ import q").timeit(number=dotimes*10)
print("q.enqueue : %d times %10.2f" %(dotimes*10,t1x))
t2y = timeit.Timer('qr.enqueue(4)', "from __main__ import qr").timeit(number=dotimes*10)
print("qr.enqueue: %d times %10.2f" %(dotimes*10,t2y))


# enqueue testing 
t1x = timeit.Timer('q.enqueue(4)', "from __main__ import q").timeit(number=dotimes)
print("q.enqueue : %d times %10.3f" %(dotimes,t1x))
t2y = timeit.Timer('qr.enqueue(4)', "from __main__ import qr").timeit(number=dotimes)
print("qr.enqueue: %d times %10.3f" %(dotimes,t2y))
t2y = timeit.Timer('qb.enqueue(4)', "from __main__ import qb").timeit(number=dotimes)
print("qb.enqueue: %d times %10.3f" %(dotimes,t2y))
t1x = timeit.Timer('q.enqueue(4)', "from __main__ import q").timeit(number=dotimes*10)
print("q.enqueue : %d times %10.2f" %(dotimes*10,t1x))
t2y = timeit.Timer('qr.enqueue(4)', "from __main__ import qr").timeit(number=dotimes*10)
print("qr.enqueue: %d times %10.2f" %(dotimes*10,t2y))
t2y = timeit.Timer('qb.enqueue(4)', "from __main__ import qb").timeit(number=dotimes*10)
print("qb.enqueue: %d times %10.2f" %(dotimes*10,t2y))

print()
print()

t1x = timeit.Timer('q.dequeue()', "from __main__ import q").timeit(number=dotimes)
print("q.dequeue : %d times %10.3f" %(dotimes,t1x))
t2y = timeit.Timer('qr.dequeue()', "from __main__ import qr").timeit(number=dotimes)
print("qr.dequeue: %d times %10.3f" %(dotimes,t2y))
t2y = timeit.Timer('qb.dequeue()', "from __main__ import qb").timeit(number=dotimes)
print("qb.dequeue: %d times %10.3f" %(dotimes,t2y))

t1x = timeit.Timer('q.dequeue()', "from __main__ import q").timeit(number=dotimes*10)
print("q.dequeue : %d times %10.3f" %(dotimes*10,t1x))
t2y = timeit.Timer('qr.dequeue()', "from __main__ import qr").timeit(number=dotimes*10)
print("qr.dequeue: %d times %10.3f" %(dotimes*10,t2y))
t2y = timeit.Timer('qb.dequeue()', "from __main__ import qb").timeit(number=dotimes*10)
print("qb.dequeue: %d times %10.3f" %(dotimes*10,t2y))

# q.enqueue : 10000 times      0.024
# qr.enqueue: 10000 times      0.003
# q.enqueue : 100000 times       3.49
# qr.enqueue: 100000 times       0.03
# q.dequeue : 10000 times      0.002
# qr.dequeue: 10000 times      0.813
# q.dequeue : 100000 times      0.023
# qr.dequeue: 100000 times      5.790
# q.enqueue : 10000 times      0.937
# qr.enqueue: 10000 times      0.003
# q.enqueue : 100000 times      11.31
# qr.enqueue: 100000 times       0.03
# q.enqueue : 10000 times      1.759
# qr.enqueue: 10000 times      0.007
# qb.enqueue: 10000 times      0.013
# q.enqueue : 100000 times      19.92
# qr.enqueue: 100000 times       0.04
# qb.enqueue: 100000 times       0.03


# q.dequeue : 10000 times      0.004
# qr.dequeue: 10000 times      1.974
# qb.dequeue: 10000 times      0.004
# q.dequeue : 100000 times      0.026
# qr.dequeue: 100000 times     11.894
# qb.dequeue: 100000 times      0.041