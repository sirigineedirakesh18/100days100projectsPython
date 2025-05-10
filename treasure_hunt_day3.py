print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You're at a crossroad. Where do you want to go? Type 'left' or 'right'.")
choice1 = input().lower()
if choice1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    print("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    choice2 = input().lower()
    if choice2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        print("One red, one yellow and one blue. Which colour do you choose?")
        choice3 = input().lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You are Eaten by beasts,Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    elif choice2 == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("You chose an option that doesn't exist. Game Over.")
elif choice1 == "right":
    print("You fell into a hole. Game Over.")
else:
    print("You chose a direction that doesn't exist. Game Over.")