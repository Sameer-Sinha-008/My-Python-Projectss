import time
from datetime import datetime

print("=========================================")
print("          WELCOME TO OLABER")
print("=========================================")

def peak():
    now = datetime.now()
    current_hour = now.hour
    
    if 17 <= current_hour < 21:
        return True
    else:
        return False

class Vehicle:
    def __init__(self, model_name, base_charge):
        self.model_name = model_name
        self.base_charge = base_charge
        
    def calculate_fare(self, distance):
        is_peak = peak()
        
        if is_peak == True:
            rate = 80
        else:
            rate = 50
            
        total_fare = self.base_charge + (distance * rate)
        return total_fare

class MiniCab(Vehicle):
    def __init__(self):
        super().__init__("Mini Cab", 10)
        self.capacity = 3

class XLCab(Vehicle):
    def __init__(self):
        super().__init__("XL Cab", 10)
        self.capacity = 4

# While loop for Persons validation
persons = int(input("Enter The Number Of Persons: "))
while persons <= 0:
    print("❌ Error: Number of persons must be at least 1!")
    persons = int(input("Please enter valid number of persons: "))

# While loop for Distance validation
Distance = float(input("Enter Distance You Wanna Travel (in km): "))
while Distance <= 0:
    print("❌ Error: Distance must be greater than 0!")
    Distance = float(input("Please enter valid distance in km: "))

# Cab allocation based on capacity
if persons <= 3:
    cab = MiniCab()
elif persons >= 4:
    cab = XLCab()
else:
    cab = None

if cab:
    fare = cab.calculate_fare(Distance)
    time.sleep(2)
    print("\n--- Cab Booked Successfully! ---")
    print("Vehicle Model:", cab.model_name)
    print("Initial Estimated Fare: ₹", fare)
    
    # Mid-Trip Destination Change Logic with While Loop
    print("\n...Trip in progress...")
    time.sleep(2)
    extend = input("\nDo you want to extend your route mid-trip? (yes/no): ").strip().lower()
    
    if extend == 'yes':
        extra_distance = float(input("Enter extra distance in km: "))
        while extra_distance <= 0:
            print("❌ Error: Extra distance must be greater than 0!")
            extra_distance = float(input("Please enter valid extra distance: "))
            
        Distance += extra_distance
        fare = cab.calculate_fare(Distance)
        print("\nUpdating route and calculating fare...")
        time.sleep(2)
        print("Updated Total Distance:", Distance, "km")
        print("Final Updated Fare: ₹", fare)
    
    time.sleep(1)
    print("\nTrip Finished! Thanks for riding with Olaber. 🚗💨")
