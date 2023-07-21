import random

#Write a program that generates and prints 100 random integers between -4 and 4

#for i in range(100):
    #print(int(random.randrange(-4,4)))

#Write a guessing game

choice = ""
guess = ""
rng = random.randrange(101)
guesses = 0
cheat = False
while choice != "n" and guess != "q":
    print("This is a guessing game where I choose a number between 0 and 100")
    while guess != rng and guess != "q" or guess == "r" or guess == "s":
        guess = (input("Guess what my secret number is: "))
        
        if guess == "s":
            set = int(input("What number should be the range of his secret number: "))
            rng = random.randrange(set)
            cheat = True

        if guess == "r":
            rng = random.randrange(101)
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
            
    if cheat == True and guess != "q" and guess != "r" and guess != "s":
        guess = ""
        rng = random.randrange(101)
        print("Did you cheat or something? It took you",guesses,"guesses.")

    elif guess != "q" and guess != "r" and guess != "s":
        guess = ""
        rng = random.randrange(101)
        print ("Nicely done mate, very cool. It took you",guesses,"guesses.")

    while choice != "n" and choice != "y" and guess != "q" and guess != "r" and guess != "s":
        choice = input("Do you wish to play again? (y/n)")

if choice == "n" or guess == "q":
    print("Buh bye!")