# no_of_wheels = 4
# mileage = 20.9
# no_of_airbags = 5
   

# def moveForward():
#     print('Car is moving')

# def moveBackward():
#     print("Car is moving backward!")

class Car:
    def __init__(self, no_of_wheels,mileage,no_of_airbags, carname):   #constructor  new object create avum 
        print("this is a constructor!")
        # self.no_of_wheels = 4   #value initiaze
        # self.mileage = 20.9
        # self.no_of_airbags = 5

        self.no_of_wheels = no_of_wheels 
        self.mileage = mileage
        self.no_of_airbags = no_of_airbags 
        self.carname = carname
    
    def __del__(self):
        print("This is a destructor!" , id(self))

    def moveForward(self, speed):
        print('Car is moving', speed ,"speed")

    def moveBackward(self):
        print("Car is moving backward!")
    
    def __str__(self):
        return (self.carname)

# car1 = Car()  #instance of class - object: Instantiation
# print(car1.no_of_wheels)
# print(car1.mileage)


# car2 = Car()  #instance of class - object: Instantiation
# car2.no_of_wheels = 8
# car2.mileage = 9
# print(car2.no_of_wheels)
# print(car2.mileage)
# print(car2.moveForward(100))
        
# car1 = Car(4,15,2)
# print(car1.no_of_wheels,car1.mileage,car1.no_of_airbags)



