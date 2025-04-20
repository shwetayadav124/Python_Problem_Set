#1) create a class "Programmer" for storing information of few programmers working at Microsoft.

'''class Programmer:
    company="Mocrosoft"
    
    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary
        print(f"Information of {self.name}")

    def getInfo(self):
        print(f"Company is {self.company}\nThe name is {self.name}, language is {self.language} and salary is {self.salary}")
harry=Programmer("harry","python",1250)
harry.getInfo()
rohan=Programmer("rohan","javascript",1350)
rohan.getInfo()
akshay=Programmer("akshay","java",1450)
akshay.getInfo()'''

#2) write a class calculator to find square, cube and square root of a number
'''class calculator:
    def __init__(self,number):
        self.number=number
    def square(self):
        print(f"square is {self.number} * {self.number} = {self.number**2}")

    def cube(self):
        print(f"cube is {self.number} * {self.number}* {self.number} = {self.number**3}")
    
    def squareRoot(self):
        print(f"squareRoot is {self.number ** 0.5}")
        
a=calculator(4)
a.square()
a.cube()
a.squareRoot()'''

'''3) create a class with a class attribute a; create an object from it and set 'a' directly using 
object.a=o. Does this change the class attribute.'''

'''class Demo:
    a=10
o=Demo()
print(o.a) #prints 10
o.a=19
print(o.a) #prints 19
#it does not change the class attribute  '''

# 4) add a static mehtod to 2nd question to greet the user with hello

'''class calculator:
    def __init__(self,number):
        self.number=number
    def square(self):
        print(f"square is {self.number} * {self.number} = {self.number**2}")

    def cube(self):
        print(f"cube is {self.number} * {self.number}* {self.number} = {self.number**3}")
    
    def squareRoot(self):
        print(f"squareRoot is {self.number ** 0.5}")

    @staticmethod
    def greet():
        print("Hello there!")    
a=calculator(4)
a.square()
a.cube()
a.squareRoot()
a.greet() '''

'''5) write a class Train which has methods to book a ticket,get status(no.of seats)
and get fare information of train running under Indian Railways.'''

'''from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"Ticket booked for train {self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time")
    def getFare(self,fro,to):
        print(f"Ticket fare for train {self.trainNo} from {fro} to {to} is {randint(222,8894)}")
t=Train(12345)
t.book("pune","mumbai")
t.getStatus()
t.getFare("pune","mumbai") '''


'''6) can you change the self-parameter inside a class to something else (say "harry").
Try changing self to "slf" or "harry" and see the effects.'''

'''from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo
    def book(harry,fro,to):
        print(f"Ticket booked for train {harry.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time")
    def getFare(self,fro,to):
        print(f"Ticket fare for train {self.trainNo} from {fro} to {to} is {randint(222,8894)}")
t=Train(12345)
t.book("pune","mumbai")
t.getStatus()
t.getFare("pune","mumbai")
#it does not change anything '''