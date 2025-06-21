# class car:
#     colour = "black"
#     engine = "v8"
#     def start(self):
#         print("Car is starting")

# car_1 = car()
# car_1.start()

# class const_Dest:
#     x = 0
#     def __init__(self, color , type):
#         self.color = color
#         self.type = type
#         print("Constructor created")
#     def __del__(self):
#         print("Destructor Used")
#     def __delattr__(self, name):
#         pass

# cd = const_Dest("Blakish-gray", "Sedan")
# print(cd.type , cd.color)



#Functional Oriented Programming
# def greet(name):
#     print("Hey!!" , name)
# print(greet("Rahul"))    
# #Object Oriented Programming
# class greets:
#     name = ""
#     def __init__(self , nm):
#         self.name = nm
#         print("Hello, ", self.name)
# c = greets("Harry")
# print(c.name)


#Inheriatnce

class Cars:
    def __init__(self , Wheels , engine , color):
        self.Wheels = Wheels
        self.engine = engine
        self.color = color
        print("The Car have ", self.Wheels , " wheels" , self.engine , " engine" , self.color , " color")
    def __del__(self):
        print(" Destructor ")

class Sedan(Cars):
    def ModelADV(self):
        # super().__init__(Wheels, engine, color)
        print("The Sedan Car have ", self.Wheels , " wheels" , self.engine , " engine" , self.color , " color")
    
# car_1 = Cars(4,"v8", "Dark-Bluish")
# print("Cars classs ", car_1)
# car_2 = Sedan(car_1.Wheels , car_1.engine , "Dark-reddish" )
# car_2.ModelADV()


#MultiLevel
class HondaAmaze():
    def Compliments(self):
        print("This is an amazing car having the engine", self.engine , " which is considerded as fastest")

# car_3 = HondaAmaze(4, "v9", "Metallic-Black")
# print(car_3.ModelADV())
# print(car_3.Compliments())

#Multiple
# class HondaCivic(Sedan,Cars ): #As i took honda amaze it automatically gave me Sedans Properties too
#     def callALL(self):
#         print("Okay this is a sedan car")
      

# car_4 = HondaCivic(4, "v12" , "Abbysal-Black")
# car_4.ModelADV()
# car_4.callALL()


#Data Hiding

class greeting:
    def __init__(self):
        pass
    def __A1_(self): # using half dundder __Var_ sets the variable , function to private only accecaible through class
        print("Hello from A1")
    def _B2_(self
             ):
        print("Hello from B2")

c = greeting()
# print(dir(c))
# c.__A1_()
c._greeting__A1_()
