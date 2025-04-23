# 1) create two virtual environments, install few packages in the first one.  How do you install the same packages in the second environment?

'''python -m virtualenv env1    #to create a virtual environment 1

 python -m virtualenv env2    #to create a virtual environment 2

 .\env1\Scripts\activate.ps1     #to activate the virtual environment 1

  pip install pandas
  pip install pyjokes

  pip freeze     #to list the installed packages
  pip freeze > requirements.txt     #to create a requirements.txt file
  deactivate    #exit the virtual environment

 .\env2\Scripts\activate.ps1    #to activate the virtual environment 2

pip install -r requirements.txt    #to install the requirements of the first environment
deactivate    #exit the virtual environment'''


# 2) write a program to input name, marks and phone number of a student and format it using the format function like below:
#  "The name of the student is harry, his marks are 72 and phone number is 111111111"

'''name=input("enter name :")
marks=int(input("enter marks :"))
phone=int(input("enter phone number :"))

a="The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phone)
print(a)'''

# 3) A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

'''table=[str(7*i) for i in range(1,11)]
a="\n".join(table)
print(a)  '''

# 4) write a program to filter a list of numbers which are divisible by 5

'''l=[5,8,9,10,45,32,85]
a=lambda x:x%5==0
f=filter(a,l)
print(list(f))'''

# 5) write a program to find the maximum of the numbers in a list using the reduce function

'''from functools import reduce
l=[1,2,333,4,5]

def greater(a,b):
    if(a>b):
        return a
    return b

r=reduce(greater,l)
print(r) '''

# 6) Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv

'''pip freeze > requirements.txt     #to create a requirements.txt file
python -m virtualenv env3    #to create a virtual environment 3

 .\env3\Scripts\activate.ps1     #to activate the virtual environment 3

pip install -r requirements.txt    #to install the requirements of the first environment
deactivate    #exit the virtual environment'''

# 7) Explore the 'Flask' module and create a web server using Flask and Python.

'''from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run() '''