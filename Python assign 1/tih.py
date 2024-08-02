"Chose your own adveture"
name  = input("Type your name: ")
print(f"Welcome {name}!")

answer = input("You are on a dirty road,it has come to an end. Which way do you want to go?").lower()

if answer == "left":
    answer = input("You come a cross the river you can walk around it or swim across? Type walk to walk around it or swim to swim across it: ").lower()
    if answer == "swim":
        print("You swam across the water and you were eaten by alligator")
    elif answer == "walk":
        print("You walked for many miles across the pool/river and you run out of water so you lose the game")
    else:
        print("Not a valid option you lose!")

elif answer == "right":
    answer = input("You come across the bridge which looks wobbly, do you want to cross it or head back(cross/back)?").lower()
    if answer == "back":
        print("You go back ,You waste your fuel")
    elif answer == "cross":
        answer = input("You cross the bridge to meet with strangers.Do you talk with them (Y/N)?").lower()
        if answer == "yes":
            print("You seak with the starnger and they give you the right direction to your destination and you WIN!")

        elif answer == "no":
            print("You ignore the stranger and the get offended and you LOSE!")

        else:
            print("Not a valid option you lose!")



    else:
        print("Not a valid option you lose!")


else:
    print("You have enter the invalid answer, You lose!")
print(f"Thank you {name} for trying:")
