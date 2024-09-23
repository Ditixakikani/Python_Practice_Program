class Vehicle:
    color="white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
school_bus=Bus("school volvo",12,50)
print(school_bus.color,school_bus.name,"speed:",school_bus.max_speed)
car=Car("Audi Q5",240,18)
print(car.color,car.name,"speed:",car.max_speed,"mileage:",car.mileage)
    