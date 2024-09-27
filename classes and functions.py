#class - used to make blueprints for our object


# CREATING OBJECTS
'''
class className:
    attributes
    purpose / functions

Identifier = className()
print(Identifier.attribute)
'''

from typing import Any


class Character:
    name = "Name"
    hp = 50
    atk = 12
    lvl = 1

characterOne = Character()
characterTwo = Character()
characterOne.name = "Nissy"
characterTwo.name = "Jed"
#print(characterOne.name)
#print(characterTwo.name)


# CONSTRUCTORS - used to initialize objects, put values on its attributes when it is created
'''
class objectName:
    def __init__(self):
        #initialize code
'''

#SELF PARAMETER - parameter of __init__ is pertaining to itslef the object that is being created

class Character:
    def __init__(self, name, hp, mp, atk, lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.lvl = lvl
        #print("Created " + self.name)
charOne = Character("Nissy", 100, 2300,6000,24)

# OBJECT FUNCTIONS - function declared inside an object, represent purpose of object
'''
class objectName:
    def __init__(self):
        #initialize code
    def objFunc(self)
        #do something
'''

class Animal:
    def __init__(self, type, voice):
        self.type = type
        self.voice = voice
    
    def speak(self): #need may self, FIRST PARAMETER TO ALL OBJECT FUNCTIONS\
        print(self.voice)

    def introduceSelf(self):
        print("I am a " + self.type)

aOne = Animal("Dog", "Arf")
#aOne.introduceSelf()
#print(aOne.voice)

# SDPT SOLUTIONS EXERCISE

class User:
    def __init__(self, fName, lName,likesCount, friendList):
        self.fName = fName
        self.lName = lName
        self.likesCount = likesCount
        self.friendList = friendList

    def introduce(self):
        print(f'Hi I am {self.fName} {self.lName}')

    def fullProfile(self):
        print(f'Full Name: {self.fName} {self.lName}')
        print(f'Likes    : {self.likesCount}')
        print(f'Friends  :')
        #for friend in self.friendList:
            #print('-' + friend)


userOne = User("Jannice", "Datingaling", 25, ["Yuan", "Shia", "Jayn"])

userOne.introduce()
userOne.fullProfile()

# INHERITANCE - allows a child class to inherit method and attributes from a parent class
# used to create variatons of objects
# PARENT CLASS - called base class of super class
# CHILD CLASS - have the same functions and attributes pero pwedeng magkaron ng bago

'''
class parentClassName:
    def __init__(self):

'''

class Person:
    def __init__(self, firstName, lastName):
        self.firstname = firstName
        self.lastname = lastName

    def introduce(self):
        print("hi I am " + self.firstname + " " + self.lastname)

# CHILD CLASS
class Student(Person):
    pass

pOne = Person("David", "SDPT")
pOne.introduce()

sOne = Student("nissy", "SDPT")
sOne.introduce()

# OVERRIDING CONSTRUCTOR **********************************************

'''
class parentClassName:
    def __init__(self):
        #initialize code
    def objFunc(self):
        #initialize code

class childClassName(parentClassName):
    def __init__(self, attributes):
    super().__init__(attributes)
    #additional attributes
'''
# super - can only be used in child
class Student(Person):
    def __init__(self, firstName, lastName, sectionYear):
        super().__init__(firstName, lastName)
        self.sectionYear = sectionYear
pOne = Person("Nissy", "Elarmo")
sOne = Student("Jed", "Dtgalng" , 2024)

# OVERRIDING FUNCTION ******************************************************
'''
class parentClassName:
    def __init__(self):
        #initialize code
    def objFunc(self):
        #do something

class childClassName(parentClassName):
    def __init__(self):
        #initialize code
    def objFunc(self):
        #do something
'''
class Student(Person):
    def __init__(self, firstName, lastName, sectionYear):
        super().__init__(firstName, lastName)
        self.sectionYear = sectionYear
    def introduce(self):
        print("hi I am " + self.firstname + " " + self.lastname + " from " + str(self.sectionYear))

pOne = Person("nissy", "elarmo")
sOne = Student("jed", "dtnglng", 2101)
print("********************OVERRIDING FUNCTIONS **************************************")
sOne.introduce()        

# CUSTOMIZING OVERRODE FUNCTIONS ********************************************************
'''
class parentClassName:
    def __init__(self):
        #initialize code
    def objFunc(self):
        #do something

class childClassName(parentClassName):
    def __init__(self):
        #initialize code
    def objFunc(self):
        super().objFunc()
        #do something
'''

class Student(Person):
    def __init__(self, firstName, lastName, sectionYear):
        super().__init__(firstName, lastName)
        self.sectionYear = sectionYear
    def introduce(self):
        super().introduce()
        print("From " + str(self.sectionYear))

class Employee(Person):
    def __init__(self, firstName, lastname, salary):
        super().__init__(firstName,lastname)
        self.salary = salary

    def introduce(self):
        super().introduce()
        print("My salary is " + str(self.salary))

pOne = Person("Nissy", "Elarmo")
sOne = Student("Jed", "dtnglng", 2101)
eOne = Employee("Patrick", "Macaraig", 3000)

print("********************CUSTOMIZING OVERRODE FUNCTIONS **************************************")
pOne.introduce()
sOne.introduce()
eOne.introduce()

# ADDING FUNCTION - DAPAT HINDI KAPANGALAN PARA HINDI MAOVERRITE

class Student(Person):
    def __init__(self, firstName, lastName, sectionYear):
        super().__init__(firstName, lastName)
        self.sectionYear = sectionYear
    def introduce(self):
        super().introduce()
        print("From " + str(self.sectionYear))
    def saySection(self):
        print("My section is " + self.secionYear)

class Employee(Person):
    def __init__(self, firstName, lastname, salary):
        super().__init__(firstName,lastname)
        self.salary = salary

    def introduce(self):
        super().introduce()
        print("My salary is " + str(self.salary))
    


sOne.saySection()
