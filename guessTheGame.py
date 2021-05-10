import random

rand = random.randrange(1,9)

for i in range(5):
    guess = int(input("guess a number between 1 and 9")) 

    if guess == rand :
        print("you have guessed it right") 
        break
    else :   
        print ("you missed!! by", rand-guess)    