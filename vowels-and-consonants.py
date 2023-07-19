
#check in a letter

letter = input("Please insert a letter: ")

while len(letter) > 1:
    print("That is a word")
    letter = input("Please insert a letter: ")

vowels = "aeiouyAEIOUY"
consonants = "bcdfghjkmnlpqrstvwxzBCDFGHJKMNLPQRSTVWXZ"

if letter in vowels:
    print("The letter <",letter,"> is a Vowel")

if letter in consonants:
    print("The letter <",letter,"> is a Consonant")

#check in a word or text

text = input("Enter some text: ")

vowels = "aeiouyAEIOUY"
consonants = "bcdfghjkmnlpqrstvwxzBCDFGHJKMNLPQRSTVWXZ"

v = 0
c = 0
x = 0

while x != len(text):
    if text[x] in vowels:
        v += 1
    if text[x] in consonants:
        c += 1
    x += 1

print("There are",v,"vowels in <",text,">")
print("There are",c,"consonants in <",text,">")

