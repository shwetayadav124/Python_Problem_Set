#1) write a program to find the greatest of four numbers entered by the user
'''a1=int(input("enter num1 :"))
a2=int(input("enter num2 :"))
a3=int(input("enter num3 :"))
a4=int(input("enter num4 :"))
if (a1>a2) and (a1>a3) and (a1>a4):
    print(f"{a1} is greatest")
elif (a2>a1) and (a2>a3) and (a2>a4):
    print(f"{a2} is greatest")
elif(a3>a1) and (a3>a2) and (a3>a4):
    print(f"{a3} is greatest")
else:
    print(f"{a4} is greatest")'''

'''2) write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 
33% in each subject to pass. Assume 3 subjects and take marks as an input from the user  '''

'''marks=int(input("enter marks of subject1 :"))
marks2=int(input("enter marks of subject3 :"))
marks3=int(input("enter marks of subject3 :"))
total_percent=(marks+marks2+marks3)/300*100
if total_percent>=40 and marks>=33 and marks2>=33 and marks3>=33:
    print("student has passed")
else:
    print("student has failed")'''


'''3) A spam comment is defined as a text contains the following keywords: 'make a lot of money',
'buy now','subscribe this', 'click this'. Write a program to detect these spams.'''

'''p1="make a lot of money"
p2="buy now " 
p3="subscribe this"
p4="click this"
a=input("enter comment :")
if (p1 in a) or (p2 in a) or (p3 in a) or (p4 in a):
    print("spam comment")
else:
    print("not a spam comment")'''

#4) write a program to find whether a given username contains less than 10 characters or not.

'''username=input("enter username :")
if len(username)<10:
    print("username is less than 10 characters")
else:
    print("username is greater than 10 characters")'''

#5) write a program which finds out whether a given name is present in a list or not

'''list1=["shweta","yadav","umme"]
name=input("Enter your name :")
if (name in list1):
    print("name is present in list")
else:
    print("name is not present in list")'''

'''6) write a program to calculate the grade of a student from his marks from the following scheme:

90-100:A
80-90:B
70-80:C
60-70:D     
50-60:E
<50:F'''

'''marks=int(input("enter marks :"))
if marks>90 and marks<=100:
    print("Excellent")
elif marks>80 and marks<=90:
    print("A")
elif marks>70 and marks<=80:
    print("B")
elif marks>60 and marks<=70:
    print("C")
elif marks>50 and marks<=60:
    print("D")
else:
    print("F")'''


#7) write a program to find out whether a given post is talking about "Harry" or not

'''post=input("enter post :")
if("harry" in post.lower()): #(this will give case insensitive output)
    #or 
    
if ("harry" in post):  #(this will give case sensitive output)
    print("This post is talking about harry")
else:
    print("This post is not talking about harry")'''
