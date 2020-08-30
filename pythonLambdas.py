#/Users/danielarcese/Desktop/Code/PyNotes/pythonLambdas.py

#lambda arguments : expression

x = lambda x, y: (x+y, x-y)
print(x(5,4)) 

x = lambda a : a + 10
print(x(5)) 

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def numbertimesothersquaredthendividelater(n, o):
    return lambda a : n * o * o / a

threetimessevensquaredanddividelater = numbertimesothersquaredthendividelater(3,7)

print(threetimessevensquaredanddividelater(3))