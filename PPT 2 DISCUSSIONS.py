Chapter 1 (1)
　　import keyword
　　import math
　　"print(keyword.kwlist)"
　　bool_true = True
　　numi1 = 100
　　numf1 = 1.02
　　and_operator = True and True
　　and_operator2 = True and True and False and True
　　or_operator = True or True
　　or_operator2 = True or False or False or True
　　or_operator3 = False or False
　　not_operator = not False
　　not_operator2 = not True
　　"""print(type(bool_true))
　　print(type(numi1))
　　print(type(numf1))
　　print(and_operator)
　　print(and_operator2)
　　print(or_operator)
　　print(or_operator2)
　　print(or_operator3)
　　print(not_operator)
　　print(not_operator2)"""
　　#AND OR
　　"""a = 10 > 5 == 10 and 80 < 1000
　　b = 10 > 5 == 10 or 80 < 1000"""
　　#and or
　　"""print (a)
　　print(b)"""
　　#FOR kw
　　for i in range(1,5):
　　"""print(i)
　　if i == 3:
　　print("hatdog")
　　elif i < 3:
　　print("cheese")
　　elif i >= 3:
　　print("burger")
　　else:
　　print("stick")"""
　　#DEF Functions
　　"""def myFunctions():
　　a = 53
　　if(a % 2 == 0):
　　print("This is an Ever Num")
　　else:
　　print("This is an Odd Num")
　　myFunctions()"""
　　#PI FROM MATH
　　"print(pi)" #from math import pi
　　"""print(f"{math.pi: .4f}") #import math"""
　　#input output
　　"""firstName = input("What is First Name: ")
　　lastName = input("What is your Last Name: ")
　　print("Welcome to my Class" , firstName , lastName)
　　firstNum = int(input("Enter First Number: "))
　　secondNum = int(input("Enter Second Number: "))
　　sum1 = firstNum + secondNum
　　print("The Answer is: ", sum1)"""
　　#sep="(gusto mong pang seperate like ",","---"..
　　# and so on..)
　　print("Apple", "Pen", "Pineapple", sep=",")
　　#end="" (sa huli lng magkakameron)
　　print("Apple", "Pen", "Pineapple", end="**")