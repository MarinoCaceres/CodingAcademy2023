import random
import words
from colorama import Fore
from colorama import Style

l = words.word_list

word = random.choice(l)

guess = ""
guesses = 0
i = 0

print("< Welcome to W0RDL3, the only name that wouldn't get us sued by The New York Times >")
print("Please insert a valid 5 letter word")
while guess != word and guesses < 5:
    guess = input("- ")

    while not guess in l or len(guess) != 5:
        print("That is not a valid 5 letter word")
        guess = input("- ")

    for i in range(len(guess)):
        if not guess[i] in word:
            print(Fore.RED + guess[i],": is wrong" + Style.RESET_ALL)

        if guess[i] in word and guess[i] != word[i]:
            print(Fore.YELLOW + guess[i],": is in the wrong place" + Style.RESET_ALL)
        
        if guess[i] == word[i]:
            print(Fore.GREEN + guess[i],": is right" + Style.RESET_ALL)
        
        i += 1
    guesses += 1
    
if guess == word:
    print(Fore.LIGHTGREEN_EX + "Congratulations! The word was",word)

if guesses == 5:
    print(Fore.LIGHTRED_EX + "You ran out of tries, the correct word was",word)