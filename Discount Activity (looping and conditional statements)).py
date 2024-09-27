#Activity combination of For and While loop
#Fare Discount

#0 dependent=no discount
#1-2 = 10%
#3-4 = 20%
#5 pataas = 30%

#Age
#adult(18-59) full fare
#senior(60+) 20% discount
#children(<18) 50% discount

def fareDiscount(dependents):

    discount = 0
    
    while True:
        if dependents == 0:
            discount = 0
            break
        elif 1 <= dependents <= 2:
            discount = 0.10
            break
        elif 3 <= dependents <= 4:
            discount = 0.20
            break
        else:
            discount = 0.30
            break
            
    return discount
    
def ageDiscount(age):

    discount = 0
    
    while True:
        if age < 18:
            discount = 0.50
            break
        elif age >= 60:
            discount = 0.20
            break
        else:
            discount = 0
            break
    return discount
        
passengerCount = int(input("How many passenger:" ))
fare = float(input("Full fare:" ))
    


for i in range(passengerCount):      
    print(f"\nPassenger {i + 1}:" )
    
    age = int(input("Enter your age:" ))
    dependents = int(input("Number of Dependents:" ))
    
    totalDiscount  =(fareDiscount(dependents) + ageDiscount(age))
    totalPayment = fare - (fare * totalDiscount)
    print(f"Total Payment: {totalPayment: .2f}")
    
