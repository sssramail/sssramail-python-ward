'''
class Car:
    model = "BMW"
    color = "white"

    def speedChange(self,v) :
        print("speedChange")
        self.speed = v

class Car:
    model = "BMW"
    color = "white"

    def speedChange(self,v) :
        print("speedChange")
    model = "BMW"
        self.speed = v


bmw = Car()
bmw.speedChange(20)

class Car:
    model = "BMW"
    color = "white"

bmw = Car()
benz = Car()

benz.model = "benz"
benz.color = "black"

print(bmw.model)
print(bmw.color)

print(benz.model)
print(benz.color)

class Car:
    count = 0
    speed = 0

    def speedChange(self,v) :
        Car.count += 1
        self.speed = v


bmw = Car()
benz = Car()

bmw.speedChange(100)
print("bmw speed :", bmw.speed)
print("number of speedChange :", Car.count)

benz.speedChange(120)
print("Benz speed :", benz.speed)
print("number of speedChange :", Car.count)

class Car:

    def setData(self,model,color) :
        self.model = model
        self.color = color


    def info(self):
        print("Model :", self.model, ",model:",self.color)


bmw = Car()
bmw.setData("BMW","white")
bmw.info()

class Car:

    def __init__(self,model,color) :
        self.model = model
        self.color = color

    def info(self):
        print("Model :", self.model, ",model:",self.color)

bmw = Car("BMW","white")
benz = Car("benz","black")
bmw.info()
benz.info()

class Car:
    def __init__(self,model,color) :
        self.model = model
        self.color = color
    def info(self):
        print("Model :", self.model, ",color:",self.color)


class CarDrive(Car) :
    def speedChange(self,v) :
        self.speed = v
        print("speedChange:", self.speed)


bmw = CarDrive("BMW","white")
bmw.info()
bmw.speedChange(100)

class Car:
    def __init__(self,model,color) :
        self.model = model
        self.color = color
        
    def info(self):
        print("Model :", self.model, ",color:",self.color)


class CarDrive(Car) :

    def info(self):
        print("The model of this car is %s " %self.model)
        print("The color is %s" %self.color)


    def speedChange(self,v) :
        sefl.speed = v
        print("speedChange:",self.speed)


bmw = CarDrive("BMW","white")
bmw.info()

class Character:
    def __init__(self,name,weapon) :
        self.name = name
        self.weapon = weapon
        
    def intro(self):
        print("Name :", self.name)
        print("Weapon :",self.weapon)

lugo = Character("Lugo","gun")
lugo.intro()
'''
class Character:
    def __init__(self,name,weapon) :
        self.name = name
        self.weapon = weapon
        
    def intro(self):
        print("Name :", self.name)
        print("Weapon :",self.weapon)


class Action(Character) :
    step = 0

    def move_forword(self,n):
        self.step += n
        print("Current location is %d." %self.step)
    def move_backwark(self,n):
        self.step -= n
        print("Current location is %d." %self.step)


    def turn_right():
        print("Turn right")
    def turn_left():
        print("Turn left")


lugo = Character("Lugo","gun")

lugo.intro()
