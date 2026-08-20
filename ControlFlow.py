import pyfiglet
# T = input("Enter Text you want to convert to ASCII art : ")
T = "NEHA"
ASCII_art_1 = pyfiglet.figlet_format(T,font='isometric1')
print(ASCII_art_1)

print("Welcome to the treasure hunt, Your mission is to find the treasure.")
direction = input("You choose to go left or right? :")
if direction == "right":
    print("Game Over...")
else:
    print("You have reached a stream and you see an Island")
    decision = input("Do you choose to wait for a boat or swim across the river? wait/swim:")
    if decision == "swim":
        print("Game Over...")
    else:
        print("You have reached the island through the boat you see 3 houses with red, yellow and blue doors")
        door = input("Which door do you choose? :")
        if door == "yellow":
            print("You found the treasure!")
        else:
            print("Game Over...")
