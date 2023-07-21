import random

#Write a program that generates and prints 100 random integers between -4 and 4

#for i in range(100):
    #print(int(random.randrange(-4,4)))

#Write a guessing game

choice = ""
guess = ""
rng = random.randrange(100)
guesses = 0
cheat = False
while choice != "n" and guess != "q":
    while guess != rng and guess != "q" or guess == "r" or guess == "s":
        guess = (input("Guess what my secret number is: "))
        
        if guess == "s":
            set = int(input("What number should be the range of my secret number: "))
            rng = random.randrange(set)
            cheat = True

        if guess == "r":
            rng = random.randrange(100)
            guesses = 0
            cheat = False

        if guess == "z":
            print("Dont tell anyone, but his number is",rng)
            cheat = True
        
        elif guess != "q" and guess != "r" and guess != "s":
            guess = int(guess)
            guesses += 1

            if guess > rng:
                print("Wrong lmao: My number is lower than",guess)
            if guess < rng:
                print("Wrong lmao: My number is higher than",guess)
            
    if cheat == True:
        guess = ""
        rng = random.randrange(100)
        print("Did you cheat or something? It took you",guesses,"guesses.")
        choice = input("Do you wish to play again? (y/n)")

    elif guess != "q" and guess != "r" and guess != "s":
        guess = ""
        rng = random.randrange(100)
        print ("Nicely done mate, very cool. It took you",guesses,"guesses.")
        choice = input("Do you wish to play again? (y/n)")

if choice == "n" or guess == "q":
    print("Buh bye!")