'''1) write a program to open three files 1.txt, 2.txt, 3.txt if any these files are not present,a message
without exiting the program should be printed.'''

'''try:
    with (open("1.txt","r") as f,
    open("2.txt","r") as f2,
    open("3.txt","r") as f3):
        print(f.read())
        print(f2.read())
        print(f3.read())

except Exception as e:
    print(e)
    print("The file is not present")
print("Thank You!")'''

# 2) write a program to print third, fifth and seventh element from a list using enumerate function.

'''l=[1,2,3,4,5,6,7,8,9]
for i,item in enumerate(l):
    if (i==2 or i==4 or i==6):
        print(item)'''

# 3) write a list comprehension to print a list which contains the multiplication table of a user entered number.

'''n=int(input("enter number :"))
table=[n*i for i in range(1,11)]
print(table)'''

# 4) write a program to display a/b where a and b are integers. If b=0,display infinite by handling the 'ZeroDivisionError' exception
'''try:
    a=int(input("enter number :"))
    b=int(input("enter number :"))
    print("a/b =",a/b)
except ZeroDivisionError:
    print("infinite")'''

# 5) store the multiplication tables generated in problem 3 in a file names Tables.txt

'''n=int(input("enter number :"))
table=[n*i for i in range(1,11)]
with open("Tables.txt","a") as f:
    f.write(f"Table of {n} is {str(table)}\n")
    '''
    
    
