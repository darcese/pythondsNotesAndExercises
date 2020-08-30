#Extend the program from Listing 2.15 to handle palindromes with spaces. For example, I PREFER PI is a palindrome that reads the same forward and backward if you ignore the blank characters.
from pythonds.basic import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        if ch != ' ':
            chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("rada r"))
print(palchecker("I PREFER PI"))
