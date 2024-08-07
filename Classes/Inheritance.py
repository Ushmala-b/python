class Vehicle: #Parent class 
    no_of_wheels = 4

    def moveForward(self):
        print("Vehicle is moving forward!")

class Car(Vehicle): #Child class single inheritance  / Sub class
   no_of_airbags = 3

# class Bike(Vehicle):
#     mileage = 25.0

class Bmw(Car): #multi level inheritance
    mileage = 10.0




car1 = Car()
print(car1.no_of_airbags)
print(car1.no_of_wheels)
car2 = Bmw()
print(car2.mileage)
car1.moveForward()

#types 
# single inheritance
# multi level inheritance
# multiple inheritance

'''

class Father:
    hair_color = 'white'

class Mother:
    eye_color = 'blue'
    hair_color = 'black'

class Child(Father, Mother):
    country  = 'india'

child = Child()
print(child.country)
print(child.hair_color)
print(child.eye_color)
'''








    