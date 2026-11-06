class Vehicle:
    def __init__(self,model, plate,mileage=0):
        self.model = model
        self.plate = plate
        self.__mileage = mileage
        self.value = 0
    def trip_registry(self, miles_added):
        if miles_added > 0:
            self.__mileage += miles_added
            print(f"New mileage is {self.__mileage}")
        else:
            print("Invalid trip mileage...")
    def details(self):
        print(f"Model - {self.model}\nPlate - {self.plate}"
              f"\nMileage - {self.__mileage}")
    def daily_value(self,value):
        return self.value + 100
    def renting(self,days):
        if self.__mileage > 50000:
            print(f"Total rent is{(days * self.value)*15/100}, with the discount of course!")
        else:
            print(f"Total rent is{days * self.value}")

class Car(Vehicle):
    def __init__(self,model, plate,mileage=0,doors=2):
        super().__init__(model, plate, mileage)
        self.doors = doors
    def daily_value(self,value):
        if self.doors == 4:
            return self.value +170
        else:
            return self.value +150


class Motocycle(Vehicle):
    def __init__(self,model, plate,mileage=0,cilinders=0):
        super().__init__(model, plate, mileage)
        self.cilinders = cilinders

    def show_cilinders(self):
        print(f"Cilinders - {self.cilinders}")
    def daily_value(self,value):
        if self.cilinders >= 300:
            return self.value +110
        else:
            return self.value + 80

print("\n---Part 1---\n")
little_car = Vehicle("Toyota","112334",mileage=100)

little_car.details()
little_car.trip_registry(1200)
little_car.trip_registry(-1225)
little_car.daily_value(0)

try:
    little_car.mileage = 1000000
except AttributeError:
    print("Can't change the mileage directly your sneaky bastard")
print("\n---Part 2 and 3---\n")

car = Car("Hondai", "23381",mileage=2300,doors=4)
motor = Motocycle("Toyota","239324",mileage=2000,cilinders=225)
motor.trip_registry(2252)
car.trip_registry(4000)
car.daily_value(0)
motor.show_cilinders()
motor.daily_value(0)
if isinstance(motor,Vehicle):
    print(f"It is a Vehicle")
else:
    print("It isn't a Vehicle")

Car_dealership = [Car("Hondai", "23381",mileage=2300,doors=4),
                  Motocycle("Toyota","239324",mileage=2000,cilinders=225)
                  ,Car("Toyota","112334",mileage=100)]
for Vehicle in Car_dealership:
    print(f"Model - {Vehicle.model}\nDaily Renting - {Vehicle.daily_value(0)}")
