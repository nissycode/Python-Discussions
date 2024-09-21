def fareDiscount(dependent, fare):
    discount = 0

    if dependent == 0:
        discount = 0
    elif 1 <= dependent <= 2:
        discount = 0.10
    elif 3 <= dependent <= 4:
        discount = 0.20
    else:
        discount = 0.30
            
    totalFare = fare - (fare * discount)
    return totalFare

passenger = int(input("How many passengers: "))
fare = float(input("Fare: "))

for i in range(passenger):
    print(f"\nPassenger {i+1}: ")
   f
    age = int(input("Passenger Age: "))
    dependents = int(input("Number of dependents: "))
    
    totalFare = fareDiscount(dependents, fare)
    print(f"Total fare for passenger {i+1}: {totalFare :.2f}")

