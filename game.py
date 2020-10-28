#Guessing Game
from random import randint

guessNumber = int(input("Enter the number from 1 to 5 : "))
randomNumber = randint(1,5)

print("Random number is : ",randomNumber)

if guessNumber == randomNumber :
    print("You have won")
else:
    print("You have lost")
