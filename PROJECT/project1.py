# we all have played snake,water,gun game in our childhood
# now let's make it in python
''' 1 for snake
  -1 for water
  0 for gun'''
import random
computer=random.choice([1,-1,0])
youstr=input("enter your choice :")
youDict={"S":1,"W":-1,"G":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[youstr]
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if(computer==you):
    print("It is a draw!")
else:
    if(computer==1 and you==-1):
        print("You lose!")
    elif(computer==-1 and you==1):
        print("You win!")
    elif(computer==0 and you==-1):
        print("You win!")
    elif(computer==-1 and you==0):
        print("You lose!")
    elif(computer==1 and you==0):
        print("You win!")
    elif(computer==0 and you==1):
        print("You win!")
    else:
        print("Something went wrong")