#1) write a program using function to find the greatest of three numbers
'''def greatest(a,b,c):
    if (a>b) and (a>c):
        return a 
    elif (b>c) and (b>c):
        return b
    elif (c>a) and (c>b):
        return c
    else:
        return "all are equal"
a=int(input("enter number :"))
b=int(input("enter number :"))
c=int(input("enter number :"))
print("The greatest number is ",greatest(a,b,c))'''

#2) write a python program to convert celsius to fahrenheit   formula: c=5*(f-32)/9
'''def f_to_c(f):
    return 5*(f-32)/9

f=int(input("enter temperature in fahrenheit :"))
print("temperature in celsius is ",f_to_c(f))'''

#3) how do you prevent a python print() function to print a new line at the end?

# print("a")
# print("b")
# print("c",end="")
# print("d",end="")

#4) write a recursive function to calculate the sum of first n natural numbers
'''def sum(n):
    if (n==1):
        return 1
    return sum(n-1)+n
n=int(input("enter number :"))
print("the sum of first natural numbers is ",sum(n))'''

'''5) write a program to print first n lines of the following pattern
***
**
*   for n=3'''

'''def pattern(n):
    if(n==0):
        return 
    print("*"*n)
    pattern(n-1)

n=int(input("enter number :"))
pattern(n)'''

#6) write a python function which converts inches to cms
'''def centi(n):
    return n*2.54
n=int(input("enter inches :"))
print("value in cms is : ",centi(n))'''


#8) write a python function to print multiplication table of a given number
'''def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
      
n=int(input("enter number :"))
table(n)'''