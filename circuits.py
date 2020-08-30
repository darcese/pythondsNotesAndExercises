class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class XorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a + b == 1 :
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

# NandGates work like AndGates that have a Not attached to the output

class NandGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 0
        else:
            return 1

# NorGates work lake OrGates that have a Not attached to the output.

class NorGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

class HalfAdder:
    def __init__(self, n):
        self.CarryGate = AndGate(n + " And Gate")
        self.SumGate = XorGate(n + " And Gate")
        self.pinA = None
        self.pinB = None

    def getCarryBit(self):
        return self.CarryGate.performGateLogic()

    def getSumBit(self):
        return self.SumGate.performGateLogic()

    #should over right inherited so both gate pins are set at same time
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
            self.CarryGate.pinA = self.pinA
            self.SumGate.pinA = self.pinA
        else:
            if self.pinB == None:
                self.pinB = source
                self.CarryGate.pinB = self.pinB
                self.SumGate.pinB = self.pinB
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
            self.CarryGate.pinA = self.pinA
            self.SumGate.pinA = self.pinA
        else:
            if self.pinB == None:
                self.pinB = source
                self.CarryGate.pinB = self.pinB
                self.SumGate.pinB = self.pinB

                #initialize carry Half Adder
                self.carryHalfAdder = HalfAdder("Carry Half Adder" + n)
                self.carryHalfAdder.setNextPin(self.abHalfAdder.CarryGate.performGateLogic())
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")





def main():

   a = 1
   b = 0
   c = 0
   d = 0

   g1 = AndGate("AandB")
   g1.setNextPin(a)
   g1.setNextPin(b)

   g2 = AndGate("CandD")
   g2.setNextPin(c)
   g2.setNextPin(d)


    # first part of check

   g3 = NorGate("NotAndBOrCDndD")
   g3.setNextPin(g1.getOutput())
   g3.setNextPin(g2.getOutput())
   

   print(g3.getOutput())

   g4 = NotGate("")
   g4.setNextPin(g1.getOutput())
   g5 = NotGate("")
   g5.setNextPin(g2.getOutput())
   g6 = AndGate("")
   g6.setNextPin(g4.getOutput())
   g6.setNextPin(g5.getOutput())
   print(g6.getOutput())
#    g4.setNextPin(g1.getOutput())
#    g4.setNextPin(g2.getOutput())
#    print(g4.getOutput())
   

#    g3.setNextPin(g1.getOutput())
#    g3.setNextPin(g2.getOutput())
#    print(g3.getOutput())



main()

# Create a two new gate classes, one called NorGate the other called NandGate. NandGates work like AndGates that have a Not attached to the output. NorGates work lake OrGates that have a Not attached to the output.

# Create a series of gates that prove the following equality NOT (( A and B) or (C and D)) is that same as NOT( A and B ) and NOT (C and D). Make sure to use some of your new gates in the simulation.

