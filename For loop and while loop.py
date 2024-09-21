
def fareDiscount(fare, dependents):

    discount = 0
    
    while True:
        if dependents == 0:
            discount = 0
            break
        elif 1<= dependents <=2:
            discount = 0.10
            break
        elif 3<= dependents <=4:
            discount = 0.20
            break
        else:
            discount = 0.30
            break
            
    totalFare = fare - (fare * discount)
    return totalFare
    
    
passengerCount = int(input("How many passenger:" ))
fare = float(input("Full fare:" ))
    
for i in range(passengerCount):
    print(f"\nPassenger {i + 1}:" )
    
    age = int(input("Enter your age:" ))
    dependents = int(input("Number of Dependents:" ))
    
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
    
    totalDiscount = fare * discount
    totalFare = fareDiscount(fare, dependents)
    toPay = totalFare - totalDiscount
    
    print(f"Total Payment: {totalFare: .2f}")
    print(f"Total Discount: {totalDiscount: .2f}")
    print(f"To Pay: {toPay: .2f}")
    