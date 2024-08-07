# Binding of variables and methods  getters and  setters 


class Car:
    def __init__(self, no_of_wheels,mileage,no_of_airbags, carname):   #constructor  new object create avum 
        print("This is a constructor!")
        # self.no_of_wheels = 4   #value initiaze
        # self.mileage = 20.9
        # self.no_of_airbags = 5

        self.__no_of_wheels = no_of_wheels 
        self.mileage = mileage
        self.no_of_airbags = no_of_airbags 
        self.carname = carname
    
    def __del__(self):
        print("This is a destructor!" , id(self))
    
   
       
    def __str__(self):
        return (self.carname)


    def moveForward(self, speed):
        print('Car is moving', speed ,"speed")

    def moveBackward(self):
        print("Car is moving backward!")
    
    def get_no_of_wheels(self):  # getter  private varibel inte value vanitt outise print cheyamegil we needto use a getter method 
        print("No of Wheels" ,self.__no_of_wheels )

car1 = Car(4 , 25 , 3 , "bmw")  #instance of class - object: Instantiation
# print(car1.no_of_wheels)
print(car1.get_no_of_wheels())
