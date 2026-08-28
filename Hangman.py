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
lives = 12
word = random.choice(words)
display = ["_"] * len(word)
while("_" in display and lives > 0):
    guess = input("Guess a letter :")
    for i,char in enumerate(word):
        if char == guess:
            display[i] = char
        another_display = "".join(display)
    if(guess not in word):
        lives -= 1
    if word == another_display:
        print("You won")
        break
    elif lives == 0:
        print("You lost")
        break
    print(another_display)
    print(f"You have {lives} lives left..")
print(f"The word was {word}")
