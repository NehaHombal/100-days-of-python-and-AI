import random
print("Hi Welcome to Hangman!..")
words = [
    "ghost",
    "jungle",
    "puzzle",
    "volcano",
    "elephant",
    "knight",
    "rainbow",
    "dinosaur",
    "adventure",
    "butterfly"
]
word = random.choice(words)
display = ["_"] * len(word)

lives = 10
while lives > 0:
    print("Can you guess the letters of :" + str(display))
    letter = input("Type in your letter :")

    for i, char in enumerate(word):
        if letter == char:
            display[i] = letter
            # print("Correct " + str(display))
        else:
            lives -= 1
            # print("Wrong " + str(display))

    if "_" not in display:
        print("You won!")
    else:
        print("You lose!")
        print("The word was :" + word)
