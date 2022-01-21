import random

text = input("Press enter to roll dice")
print(text)
if text == "":
    dicesides = [1, 2, 3, 4, 5, 6]
    diceoutcome = random.choice(dicesides)
    if (diceoutcome) == 1:
        print(" -------")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print(" -------")
        print(" ")
    elif (diceoutcome) == 2:
        print(" -------")
        print("| o     |")
        print("|       |")
        print("|     o |")
        print(" -------")
        print(" ")
    elif (diceoutcome) == 3:
        print(" -------")
        print("| o     |")
        print("|   o   |")
        print("|     o |")
        print(" -------")
        print(" ")
    elif (diceoutcome) == 4:
        print(" -------")
        print("| o   o |")
        print("|       |")
        print("| o   o |")
        print(" -------")
        print(" ")
    elif (diceoutcome) == 5:
        print(" -------")
        print("| o   o |")
        print("|   o   |")
        print("| o   o |")
        print(" -------")
        print(" ")
    else:
        print(" -------")
        print("| o   o |")
        print("| o   o |")
        print("| o   o |")
        print(" -------")
        print(" ")
else:
    print("You pressed some text before pressing enter")

i=0
while i<100:
    i+1
    reroll = input("Press enter to roll again or Ctrl+C to stop the program")
    print(reroll)
    if reroll == "":
            dicesides = [1, 2, 3, 4, 5, 6]
            diceoutcome = random.choice(dicesides)
            if (diceoutcome) == 1:
                print(" -------")
                print("|       |")
                print("|   o   |")
                print("|       |")
                print(" -------")
                print(" ")
            elif (diceoutcome) == 2:
                print(" -------")
                print("| o     |")
                print("|       |")
                print("|     o |")
                print(" -------")
                print(" ")
            elif (diceoutcome) == 3:
                print(" -------")
                print("| o     |")
                print("|   o   |")
                print("|     o |")
                print(" -------")
                print(" ")
            elif (diceoutcome) == 4:
                print(" -------")
                print("| o   o |")
                print("|       |")
                print("| o   o |")
                print(" -------")
                print(" ")
            elif (diceoutcome) == 5:
                print(" -------")
                print("| o   o |")
                print("|   o   |")
                print("| o   o |")
                print(" -------")
                print(" ")
            else:
                print(" -------")
                print("| o   o |")
                print("| o   o |")
                print("| o   o |")
                print(" -------")
                print(" ")
    else:
        print("You pressed some text before pressing enter")
