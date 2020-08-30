def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         if type(top) is not int or type(bottom) is not int:
             raise Exception('Numerator and Denominator have to be integers')
      
         if bottom == 0 :
             raise Exception('No Fractions with 0 in the denominator allowed now')

         if bottom < 0:
             top = top * -1
             bottom = bottom * -1

         self.numpOriginal = top
         self.denOriginal = bottom
         common = gcd(self.numpOriginal,self.denOriginal)

         self.num = int( self.numpOriginal // common)
         self.den = int(self.denOriginal // common)

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def __repr__(self):
         return '{numerator: '+str(self.num)+', denominator: '+str(self.den)+ '}'

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         
         return Fraction(newnum,newden)

     def __radd__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         
         return Fraction(newnum,newden)

     def __iadd__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         self.__init__(newnum,newden)

         return self

     def __sub__(self,otherfraction):
         newnum = self.num*otherfraction.den -  self.den*otherfraction.num
                     
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __mul__(self,otherfraction):
         newnum = self.num * otherfraction.num
                     
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum // common,newden // common)

     def __truediv__(self,otherfraction):
         newnum = self.num * otherfraction.den
                     
         newden = self.den * otherfraction.num
         common = gcd(newnum,newden)
         return Fraction(newnum //common,newden //common)


     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum


     def __gt__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum > secondnum

     def __ge__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum >= secondnum

     def __lt__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum < secondnum

     def __le__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum <= secondnum

     def __ne__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum != secondnum
        
    


    #TODO iImplement the remaining relational operators (__gt__, __ge__, __lt__, __le__, and __ne__)    


     def getNum(self):
        return self.num

     def getDen(self):
        return self.den

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)

print(gcd(4,3))