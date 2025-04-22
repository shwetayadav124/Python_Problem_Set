# 1) create a class(2-D vector) and use it to create another class representing 3-D vector

'''class Vector2D:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The 2D vector is {self.i}i + {self.j}j")
class Vector3D(Vector2D):
    def __init__(self,i,j,k):
        self.k=k
        super().__init__(i,j)

    def show(self):
        print(f"The 3D vector is {self.i}i + {self.j}j + {self.k}k")
a=Vector2D(1,2)
b=Vector3D(1,2,3)
a.show()
b.show()'''

# 2) create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to 'Dog' class.

'''class Animals:
    pass
class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")
a=Dog()
a.bark()'''

'''3) create a class 'Employee' and add salary and increment properties to it. Write a method 'salaryAfterIncrement' method
with a @property decorator with a setter which changes the value of increment based on the salary'''

'''class Employee:
    salary=234
    increment=20
   
    
    @property   
    def salaryAfterIncrement(self):
        return (self.salary+self.salary*(self.increment/100))

#new salary= old salary (1+increment/100)
#increment=(new salary/old salary -1) *100

    @salaryAfterIncrement.setter  #we can set new salary and calculate increment
    def salaryAfterIncrement(self,salary):
        self.increment= ((salary/self.salary) -1) *100
e=Employee()   
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 300
print(e.increment)'''

# 4) write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them

'''class Complex:
    def __init__(self,r,i):
        self.i=i
        self.r=r
    def __add__(self,c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self,c2):
        return Complex(self.r * c2.r - self.i * c2.i, self.r * c2.i + self.i * c2.r)
    def __str__(self): #used for representation
        return f"{self.r} + {self.i}i"

c1=Complex(1,2)
c2=Complex(3,4)
print(c1 + c2)
print(c1 * c2)'''

'''5) write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates
the sum and dot product of two vectors'''

'''class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __add__(self,other):
        result=self.i + other.i , self.j + other.j , self.k + other.k
        return result
    def __mul__(self,other):
        result=self.i * other.i + self.j * other.j + self.k * other.k
        return result
    def __str__(self):
        return f"Vector({self.i}, {self.j}, {self.k})"
v1=Vector(1,2,3)
v2=Vector(4,5,6)
v3=Vector(7,8,9)
print(v1+v2)
print(v1*v2)
print(v1+v3)
print(v1*v3)'''

# 6) write __str__() method to print the vector 7i + 8j + 10k
'''class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
v1=Vector(7,8,10)
print(v1)'''

# 7) Override the __len_() method on vector of question 5 to display the dimension of the vector
'''class Vector:
    def __init__(self,l):
        self.l=l
    
    def __len__(self): #it returns the length of the vector and the values of the vector is stored in l
        return len(self.l)
v1=Vector([1,2,3])
print(len(v1)) #output 3 '''
