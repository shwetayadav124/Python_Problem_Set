#1) write a program to print multiplication table of a given number using for loop

'''n=int(input("enter number :"))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")'''

# 2) write a program to greet all the person names stored in a list 'l' and which starts with 'S'
'''l=["Harry","Soham","Sachin","Rahul"]
for i in l:
    if i.startswith("S"):
        print(f"hello {i}")'''

#3) attempt problem 1 using while loop
'''n=int(input("enter number :"))
i=1
while(i<11):
    print(f"{n} x {i} = {n*i}")
    i+=1'''

#4) write a program to find whether a given number is prime or not
'''n=int(input("enter number :"))
for i in range(2,n):
    if(n%i)==0:
        print("number is not prime")
        break
else:
    print("number is prime")'''

# 5) write a program to find the sum of first n natural numbers using while loop
'''n=int(input("enter number :"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)'''

# 6) write a program to calculate the factorial of a given number using for loop
'''n=int(input("enter the number :"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)'''

'''7) write a program to print the following star pattern
  *
 ***
***** for n=3'''

'''n=int(input("enter the number :"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")'''

'''8) write a program to print the following star pattern
   *
   **
   *** for n=3'''

'''n=int(input("enter the number: "))
for i in range(1,n+1):
    print("*"*i,end="")
    print("")'''

'''9) write a program to print the following star pattern
***
* *
*** for n=3'''
'''n=int(input("enter the number: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")'''
    
# 10) write a program to print multiplication table of using for loops in reversed order
'''n=int(input("enter the number "))
for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")'''