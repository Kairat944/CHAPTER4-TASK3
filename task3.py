class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0
        self.fuel = 70

    def __add_distance(self,km):
        self.odometr += km
        
    def __subtract_fuel(self,liters):
        self.fuel -= liters
        
    def drive(self,km):
        
        liters = km / 10
        if liters <= self.fuel:
            #self.__add_distance(km)
            print("Let's drive!!!")
        else:
            #self.fuel == 0
            #self.__subtract_fuel(liters)
            print("Need more fuel, please, fill more!")
    
car1 = Car("Japan","Subaru",2000)
print(car1.model)
print(car1.year)
car1.drive(500)

