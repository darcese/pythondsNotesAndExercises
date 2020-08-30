class RadixNumber:
    def __init__(self,number):
        self.numStr = str(number)
        self.length = len(self.numStr)
        self.ones = int(self.numStr[self.length -1])

        if self.length == 1 :
            self.ones = int(self.numStr[0])
            self.tens = 0
            self.hundreds = 0
        if self.length == 2 :
            self.ones = int(self.numStr[1])
            self.tens = int(self.numStr[0])
            self.hundreds = 0
        if self.length == 3 :
            self.ones = int(self.numStr[2])
            self.tens = int(self.numStr[1])
            self.hundreds = int(self.numStr[0])

def radixSorter(listOfNumbers):
    radixList = []
    for number in listOfNumbers:
        radixList.append(RadixNumber(number))
     
    list1 = sorted(radixList, key=lambda x: (x.hundreds, x.tens, x.ones), reverse=True)
    list2 = []
    for number in list1:
        list2.append(number.numStr)
    
    return list2



print(radixSorter([5,55,345,32,2,99,999,9,5,65,65,3]))


