# NUMBER 1
def calculate_area(radius):
    area = 3.14 * (radius **2) # change ^ to **
    return area
r = 5
result = calculate_area(r)
print("The area of the circle is:", result)

# NUMBER 2
def get_item_from_list(my_list, index):
    if index >= len(my_list): # insert some code that will hold the error
        return "Out of range!"
    else:
        return my_list[index]

items = [1,2,3,4,5]
idx = 10
result = get_item_from_list(items, idx)
print("The item at index", idx, "is:", result)

#NUMBER 3
def check_even_or_odd(number):
    if number % 2 == 0: #change assignment sign to comparison operator
        print("The number is even")
    else:
        print("The number is odd")
        
num = 7
check_even_or_odd(num)

#NUMBER 4
def check_age(age):
    if age > 18:
        print("You are an adult")
    elif age == 18: #change assignment sign to comparison operator
        print("You are exactly 18")
    else:
        print("You are a minor") #change indentation

age_input = 18
check_age(age_input)

#NUMBER 5
def sum_of_numbers(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i] #change number into numbers
    print("The sum is:", total) #change indentation
    
num_list = [10,20,30]
sum_of_numbers(num_list)
        


