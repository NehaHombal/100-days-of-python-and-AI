# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
import random
computer = random.randint(1,2) # 0 1 2
you = int(input("rock(0), paper(1) or sissors(2)?"))
print(you)
print(computer)
if you == computer:
    print("Its a draw")
elif you == 0 and computer == 1:
    print("You Lose")
elif you == 0 and computer == 2:
    print("You Win")
elif you == 1 and computer == 0:
    print("You Win")
elif you == 1 and computer == 2:
    print("You Lose")
elif you == 2 and computer == 0:
    print("You Lose")
elif you == 2 and computer == 1:
    print("You Win")
else: 
    print("Please input 0,1 or 2 as inputs...")
# // rock and paper = paper
# // rock and sissors  = rock
# // paper and rock = paper
# // paper and sissors = sissors
# // sissors and rock = rock 
# // sissors and paper = sissors


print("adding streaks")

