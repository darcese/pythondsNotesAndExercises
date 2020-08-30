#Construct a class hierarchy for people on a college campus. 
#Include faculty, staff, and students. What do they have in common? 
#What distinguishes them from one another?

#
#import datetime
# = datetime.datetime(2020, 5, 17)

class Person:

    def __init__(self, name, gender, dateOfBirth):
        self.name = name
        self.gender = gender
        self.dateOfBirth = dateOfBirth
       

    def sleep(self, hours):
        return print("Slept for" + str(hours))
    
    def eat(self, food):
        return print("Ate " + food)

    def wentToBathroom(self,number1Or2 = 1, washedHands= True):
        bathroomString = self.name

        bathroomString += " peed" if number1Or2 == 1 else " pooed"      
        bathroomString += " and washed their hands" if washedHands else " and didnt wash their hands"
        print(bathroomString)


        
class Student(Person):
    def __init__(self,name, gender, dateOfBirth, major, year):
        super(Student, self).__init__(name, gender, dateOfBirth)

        self.major = major
        self.year = year

    def study(self):
        print(self.name + " studies " + self.major)

class Teacher(Person):
    def __init__(self,name, gender, dateOfBirth, field):
        Person.__init__(self,name, gender, dateOfBirth)

        self.field = field

    def teach(self):
        print(self.name + " teaches" + self.field)