#import timeit



#setup = 'import random \n' + \
#"random.seed('slartibartfast') \n" + \
#'s = [random.random() for i in range(1000)] \n' + \
#'timsort = list.sort'

#print(min(timeit.Timer('a=s[:]; timsort(a)', setup=setup).repeat(7, 1000)))

import timeit
from timeit import Timer
from random import randint as randint


size1 = 101
size2 = 10001
size3 = 1000001

x = {j:None for j in range(size1)}
y = {j:None for j in range(size2)}
z = {j:None for j in range(size3)}

dotimes = 1000000
  
t1x = timeit.Timer('x[100] = 4', "from __main__ import x").timeit(number=dotimes)
print("dictSize : %d , timetoset %10.3f" %(size1, t1x))
t2y = timeit.Timer('y[100] = 4', "from __main__ import y").timeit(number=dotimes)
print("dictSize : %d , timetoset %10.3f" %(size2, t2y))
t3z = timeit.Timer('z[100] = 4', "from __main__ import z").timeit(number=dotimes)
print("dictSize : %d , timetoset %10.15f" %(size3, t3z))


a = [j for j in range(size1)]
b = [j  for j in range(size2)]
c = [j  for j in range(size3)]

t1x = timeit.Timer('d = a[99]', "from __main__ import a").timeit(number=1)
print("listSize : %d , timetoset %10.3f" %(size1, t1x))
t2y = timeit.Timer('d = b[99]', "from __main__ import b").timeit(number=1)
print("listSize : %d , timetoset %10.3f" %(size2, t2y))
t3z = timeit.Timer('d = c[99]', "from __main__ import c").timeit(number=1)
print("listSize : %d , timetoset %10.15f" %(size3, t3z))

def doSeveralTimesAndSumTimes(func, doTimes):
    x = 0
    for i in range(dotimes):
        x+= func
    return x

print("TESTING DOSEVERALTIMESWRAPPER")

print(doSeveralTimesAndSumTimes(t1x, dotimes))

print("dictionary dels")
t1x = timeit.Timer('del x[100]', "from __main__ import x").timeit(number=1)
print("dictSize : %d , timetoset %10.3f" %(size1, doSeveralTimesAndSumTimes(t1x, dotimes)))
t2y = timeit.Timer('del y[100]', "from __main__ import y").timeit(number=1)
print("dictSize : %d , timetoset %10.3f" %(size2, doSeveralTimesAndSumTimes(t2y, dotimes)))
t3z = timeit.Timer('del z[100]', "from __main__ import z").timeit(number=1)
print("dictSize : %d , timetoset %10.3f" %(size2, doSeveralTimesAndSumTimes(t3z, dotimes)))

print("\n list dels \n")
t1x = timeit.Timer('del a[99]', "from __main__ import a").timeit(number=1)
print("listSize : %d , timetoset %10.3f" %(size1, doSeveralTimesAndSumTimes(t1x, dotimes)))
t2y = timeit.Timer('del b[99]', "from __main__ import b").timeit(number=1)
print("listSize : %d , timetoset %10.3f" %(size2, doSeveralTimesAndSumTimes(t2y, dotimes)))
t3z = timeit.Timer('del c[99]', "from __main__ import c").timeit(number=1)
print("listSize : %d , timetoset %10.15f" %(size3, doSeveralTimesAndSumTimes(t3z, dotimes)))

#Given a list of numbers in random order, write an algorithm that works in 𝑂(𝑛log(𝑛)) to find the kth smallest number in the list.
#Can you improve the algorithm from the previous problem to be linear? Explain.

randomList = [randint(0, 100) for  j in range(size1)]

def getKsmallestInList(list = [1,2,3], k = 1):
    newList = list.sort()
    return[k-1]

print(getKsmallestInList(randomList, 40))







#

#Devise an experiment to verify that get item and set item are 𝑂(1)
#for dictionaries.
