#strings and methods
name="shweta"
print(name[0:3])
print(name[5])
print(name[1:-1])
print(name[1:5:2]) #step
name=input("enter your name :")
print("good morning",name)
#or
print("good morning "+name)
#or
print(f"good morning {name}") #f string
a="shweta yadav"
print(a.upper())#to convert lowercase to uppercase
print(a.lower()) #to convert uppercase to lowercase
print(a.title()) #to convert first letter of each word to uppercase
print(a.strip()) #to remove spaces
print(a.split()) #to convert string to list
print(a.replace("shweta","xyz")) #to replace string
print(a.find("yadav")) #to find index
print(a.index("yadav")) #to find index
print(a.count("a")) #to count number of characters
print(a.isalnum()) #to check whether string is alphanumeric
print(a.isalpha()) #to check whether string is alphabetical
print(a.isdigit()) #to check whether string is digit
print(a.islower()) #to check whether string is lowercase
print(a.isupper()) # to check whether string is uppercase
print(a.isspace()) #to check whether string is space
print(a.endswith("av")) #to check whether string ends with "av"
print(a.startswith("sh")) #to check whether string starts with "sh"
print(a.capitalize()) #to convert first letter of string to uppercase
print(a.swapcase()) #to convert lowercase to uppercase and uppercase to lowercase
