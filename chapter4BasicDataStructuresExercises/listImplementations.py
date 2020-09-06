class StackListNode:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class StackList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self,item):
        temp = StackListNode(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def pop(self):
        current = self.head
        self.head = current.getNext()
        return current

list1 = StackList()
list1.push(1)
list1.push(2)
list1.push(3)

print(str(list1.pop().getData()))
print(str(list1.pop().getData()))

class QueueList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self,item):
        temp = StackListNode(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def pop(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        
        previous.setNext(None)
        return current
    
    

list1 = QueueList()
list1.push(1)
list1.push(2)
list1.push(3)

print(str(list1.pop().getData()))
print(str(list1.pop().getData()))

class DequeueList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def pushToFront(self,item):
        temp = StackListNode(item)
        temp.setNext(self.head)
        self.head = temp

    def pushToRear(self,item):
        temp = StackListNode(item)
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        
        current.setNext(temp)
        

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def popFromFront(self):
        current = self.head
        self.head = current.getNext()
        return current

    def popFromRear(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        
        if previous != None:
            previous.setNext(None)
        return current
    
    
print()
list1 = DequeueList()
list1.pushToFront(1)
list1.pushToFront(2)
list1.pushToFront(3)
list1.pushToFront(4)
list1.pushToRear(5)
list1.pushToRear(6)

print(str(list1.popFromFront().getData()))
print(str(list1.popFromRear().getData()))


# experiment section
import timeit
from timeit import Timer
from random import randint as randint


dotimes = 100

queueList = QueueList()
stackList = StackList()

print()

# queue takes for ever to pop from end
t1x = timeit.Timer('queueList.push(4)', "from __main__ import queueList").timeit(number=dotimes)
print("queueList.push: %d times %10.3f" %(dotimes,t1x))
t2y = timeit.Timer('queueList.pop()', "from __main__ import queueList").timeit(number=dotimes-1)
print("queueList.pop: %d times %10.3f" %(dotimes,t2y))
t1x = timeit.Timer('queueList.push(4)', "from __main__ import queueList").timeit(number=dotimes*10)
print("queueList.push: %d times %10.2f" %(dotimes*10,t1x))
t2y = timeit.Timer('queueList.pop()', "from __main__ import queueList").timeit(number=dotimes*10-1)
print("queueList.pop: %d times %10.2f" %(dotimes*10,t2y))

print ()
dotimes = 10000
# stacklist is O(1) tto push/ pop
t1x = timeit.Timer('stackList.push(4)', "from __main__ import stackList").timeit(number=dotimes)
print("stackList.push: %d times %10.3f" %(dotimes,t1x))
t2y = timeit.Timer('stackList.pop()', "from __main__ import stackList").timeit(number=dotimes-1)
print("stackList.pop: %d times %10.3f" %(dotimes,t2y))
t1x = timeit.Timer('stackList.push(4)', "from __main__ import stackList").timeit(number=dotimes*10)
print("stackList.push: %d times %10.2f" %(dotimes*10,t1x))
t2y = timeit.Timer('stackList.pop()', "from __main__ import stackList").timeit(number=dotimes*10-1)
print("stackList.pop: %d times %10.2f" %(dotimes*10,t2y))

pythonList = []
t1x = timeit.Timer('pythonList.append(4)', "from __main__ import pythonList").timeit(number=dotimes)
print("pythonList.append: %d times %10.3f" %(dotimes,t1x))
t2y = timeit.Timer('pythonList.pop()', "from __main__ import pythonList").timeit(number=dotimes-1)
print("pythonList.pop: %d times %10.3f" %(dotimes,t2y))
t1x = timeit.Timer('pythonList.append(4)', "from __main__ import pythonList").timeit(number=dotimes*10)
print("pythonList.append: %d times %10.2f" %(dotimes*10,t1x))
t2y = timeit.Timer('pythonList.pop()', "from __main__ import pythonList").timeit(number=dotimes*10-1)
print("pythonList.pop: %d times %10.2f" %(dotimes*10,t2y))


class DoublyLinkedNode:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.back = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getBack(self):
        return self.back

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def setBack(self,newback):
        self.back = newback

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        #temp = Node(item)
        #temp.setNext(self.head)
        #self.head.setBack(temp)
        #self.head = temp
        #self.head.set

        if self.head == None:
            self.head = DoublyLinkedNode(item)
            self.tail = None
            
            print("head was none")
        
        elif  self.head is not None:
            if self.tail is None:
                self.tail = self.head
                self.head = DoublyLinkedNode(item)
                self.head.setNext(self.tail)
                print(self.head.getNext().getData())
                self.head.setBack(self.tail)
                self.tail.setBack(self.head)
                self.tail.setNext(self.head)
                print("tail was none")
            else:
                prevHead = self.head
                newHead = DoublyLinkedNode(item)
                #print(newHead.getData())
                #print(prevHead.getBack().getData())

                prevHead.setBack(newHead)
                self.tail.setNext(newHead)
                #print(self.tail.getData())

                newHead.setNext(prevHead)
                newHead.setBack(self.tail)
                self.head = newHead
                
                print(self.head.getNext().getData())
                print(self.head.getBack().getData())
                # print('head' + str(self.head.getData()))
                # print(type(self.head))
                # print('head back' + str(self.head.getNext().getData()))
                # print('head next' + str(self.head.getBack().getData()))
                # print('tail' +str(self.tail.getData()))
                # print("both were not already none")
                

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def popTail(self):
        oldTail = self.tail
        self.tail = oldTail.getBack()
        self.head.setBack(self.tail)
        self.tail.setNext(self.head)
        return oldTail


    def popHead(self):
        oldHead = self.head
        self.head = oldHead.getNext()
        self.head.setBack(self.tail)
        self.tail.setNext(self.head)
        return oldHead
#28 stacklist push/ pop are O(1)

doubly = DoublyLinkedList()
doubly.add(1)
doubly.add(2)
doubly.add(3)
doubly.add(4)
doubly.add(5)


print(str(doubly.popHead().getData()))
print(str(doubly.popHead().getData()))
print(str(doubly.popTail().getData()))
print(str(doubly.popTail().getData()))


