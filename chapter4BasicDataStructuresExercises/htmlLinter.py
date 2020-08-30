testString = "<html> \
   <head> \
      <title>\
         Example\
      </title>\
   </head>\
   <body> \
      </h1>Hello, world</h1>\
   </body>\
</html>"


def closingAndOpeningTagChecker(string):
    from pythonds.basic import Stack

    newString = string.split(">")
    newStack = Stack()
    for string in newString:
        try:
            if "/" in string:
                newStack.pop()
            else:
                newStack.push(string)
            if string == "":
                newStack.pop()
        except IndexError:
            return False
      

    return newStack.isEmpty()

print(closingAndOpeningTagChecker(testString))

