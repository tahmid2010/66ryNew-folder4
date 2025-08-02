
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def fare(self):
        
        base_fare = super().fare()
        

        maintenance_charge = 0.10 * base_fare
        
      
        total_fare = base_fare + maintenance_charge
        return total_fare

bus_ride = Bus(50)


final_fare = bus_ride.fare()
print(f"The total fare for the bus ride is {final_fare}")