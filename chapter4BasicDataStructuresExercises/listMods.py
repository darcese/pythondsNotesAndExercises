#characters.

#To implement the length method, we counted the number of nodes in the list. An alternative strategy would be to store the number of nodes in the list as an additional piece of data in the head of the list. Modify the UnorderedList class to include this information and rewrite the length method.
# Why store it in the head. Why not on the list itself?

#Implement the remove method so that it works correctly in the case where the item is not in the list.
#One question that often arises is whether the two cases shown here will also handle the situation where the item to be removed is in the last node of the linked list. We leave that for you to consider.

class Node:
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

#Implement the remaining operations defined in the UnorderedList ADT (append, index, pop, insert).
class UnorderedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.length +=1

    def size(self):
        return self.length

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def index(self,item):
        index = 0
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
                
            else:
                current = current.getNext()
                index +=1

        return index

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                if current.getNext() == None:
                    return "Item not in list"
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.length -= 1

    def __str__(self): 
        listOfData = []
        current = self.head
        while current != None:
            listOfData.append(current.getData())
            current = current.getNext()
        return str(listOfData)
    #Implement the remaining operations defined in the UnorderedList ADT (append, index, pop, insert).

    def append(self,item):
        current = self.head
        previous = None
        if current == None:
            self.add(item)
            return 
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(item)
    
    def pop(self):
        current = self.head
        previous = None
        if current == None:
            return
        while current.getNext() != None:
            previous = current
            current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        return(current)
        self.length -= 1

    def insert(self,item,index):
        if index > self.size():
            self.append(item)
            return
        if index == 0:
            self.add(item)
        current = self.head
        previous = None
        currentIndex = 0
        while currentIndex != index :
            previous = current
            current = current.getNext()
            currentIndex += 1



        if previous != None:
            previous.setNext(item)
        item.setNext(current)


        

        


  #Implement the remaining operations defined in the UnorderedList ADT (append, index, pop, insert).
  # do the same for ordered
  # for ordered i dont like insert, and append since its ordered and we have add that puts things in the right order
  # will do index and pop though
class OrderedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.length

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False

        #modified to deal with duplicates by not adding them
        #if self.search(item) == True:
        #    return ""

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        self.length += 1

    def remove(self,item): # remove just removes 1 instance of a duplicate for now. to remove multiple
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
                while current.getNext().getData() == item:
                    current = current.getNext()
                    self.length -= 1
            else:
                if current.getNext() == None:
                    return "Item not in list"
                previous = current
                current = current.getNext()

        if previous == None:

            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.length -= 1

   
    def __str__(self): 
        listOfData = []
        current = self.head
        while current != None:
            listOfData.append(current.getData())
            current = current.getNext()
        return str(listOfData)

    def index(self,item):
        index = 0
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
                
            else:
                current = current.getNext()
                index +=1

        return index

    def pop(self):
        current = self.head
        previous = None
        if current == None:
            return
        while current.getNext() != None:
            previous = current
            current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        return(current)
        self.length -= 1

    
        

mylist = OrderedList()

mylist.add(31)
mylist.add(31)
mylist.add(77)
newNode = Node(45)
#mylist.append(newNode)
print(mylist.size())
print(mylist.index(45))

mylist.remove(31)

print(str(mylist))
print(str(mylist.pop().getData()))
print(str(mylist))

mylist.add(35)
mylist.add(39)
newNode2 = Node(37)
#mylist.insert(newNode2,0)
print(str(mylist))
