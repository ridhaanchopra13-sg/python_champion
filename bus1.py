class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(vehicle):
    pass
School_bus = Bus("Volvo",180,4321)
print("Name is:",School_bus.name,"Max_speed is: ",School_bus.max_speed,"Mileage is: ",School_bus.mileage)