import random

num = random.randint(1,100)

tries = 0 

while True :
    guess = int(input("Guess your no. btw 1 to 100:-"))
    
    if num == guess:
        tries += 1
        print(f"You guessed the right no. after {tries} tries and the no. is {guess}")
        break

    elif num < guess :
        print("guess a liitle lower no.")
        tries += 1

    elif num > guess :
        print( " guess a little higher no.")
        tries += 1

    else:
        print("you are wrong")