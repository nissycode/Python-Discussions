#FOR LOOP

# color = {"red", "orange","green"}
# print(type(color))
"""
#break

for i in color:

    if i == "green":
        break
    print(i)

#continue

    if i == "green":
        continue
    print(i)
"""
"""
#specific print
for i in color:
    print(i)

for i in "red":
    print(i)

#range and concatination

for x in range(3):
    print(x)

for x in range(3):
    print(f"NUMBER {x}")
"""

"""
for value in sequence:
    body of your loop
"""

#starting & endpoint & skipping point
# for x in range(1,10,2):
#     print(f"Number {x}")

#for loop else condition
# for x in range(1,10):
#     if x == 3: break
#     print(f"Number {x}")
#
# else:
#     print("E N D")

# for x in range(1,10):
#     if x == 11: break
#     print(f"Number {x}")
#
# else:
#     print("E N D")

#nested for loop
# color = ["pink","black","blue"]
# shape = ["circle","square","triangle"]
#
# for c in color:    #outer loop
#     for s in shape:    #inner loop
#         print(c,s)

#WHILE LOOP
#while condition:
    #BODY OF WHILE LOOP

#increment

# i = 10
# while i < 20:
#     print(i)
#     i += 1

#if statement & break   #starting point i, while condition hanggang san, if i hanggang ilan
# i = 10
# while i < 13:
#     print(i)
#     if i == 13:
#         break
#     i += 1

#continue & else
# i = 10
# while i < 20:
#     print(i)
#     i += 1
# else:
#     print("i is not less than 20")


#EXPECTED OUTPUT IN FOR AND WHILE FARE DISCOUNT

#0 dependent = no discount
#1-2 = 10%
#3-4 = 20%
#5 pataas = 30%

#adult (18-59) full fare
#senior (60 pataas) 20% discount
#children (1<18) 50% discount

