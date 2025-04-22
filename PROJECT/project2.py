'''we are going to write a program that generates a random number and asks the user to guess it.
If the player's guess is higher than the random number, the program should display "Lower number please!"
If the player's guess is lower than the random number, the program should display "Higher number please!"
If the player's guess is equal to the random number, the program should display the number of guesses the player used to arrive at the number

Hint: Use the random module. '''

from random import randint
n=randint(1,100)
a=0
guesses=0
while(a!=n):
    a=int(input("Guess the number :"))
    guesses+=1
    if(a>n):
        print("Lower number please!")
    elif(a<n):
        print("Higher number please!")
print(f"You guessed the number {n} in {guesses} guesses")


