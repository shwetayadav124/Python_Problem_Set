a=3
b=4
c=a+b
print(c)
print(type(c)) #to find the type of variable

#arithmetic operator 
a=4
z=2
y=a/z
print("quotient :",y)
x=a%z
print("remainder :",x)

# check the type of variable assigned using input() function
s=input("enter number :")
print(type(s))
r=float(s)
print(type(r))
d=int(input("enter number :"))
print(type(d))

# use comparison operator to find out whether a given variable f is greater than g, or not. Take f=34 and g= 80
f=34
g=80
l=f>g 
print(l)

# write a python program to find an average of two numbers entered by the user
o=int(input("enter num1 :"))
p=int(input("enter num2 :"))
v=(o+p)/2
print(v)



# write a python program to calculate the square of a number entered by the user
h=int(input("enter number :"))
k=h*h
#or k=h**2 by this method we can get value for h**20 or any other power
print(k)