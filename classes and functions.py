#class - used to make blueprints for our object


# CREATING OBJECTS
'''
class className:
    attributes
    purpose / functions

Identifier = className()
print(Identifier.attribute)
'''

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
        for friend in self.friendList:
            print('-' + friend)


userOne = User("Jannice", "Datingaling", 25, ["Yuan", "Shia", "Jayn"])

userOne.introduce()
userOne.fullProfile()





