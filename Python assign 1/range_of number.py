import random

top_number = input("Enter the maximum number: ")
if top_number.isdigit():
    top_number = int(top_number)

    if top_number <= 0:
        print("enter a number above 0")
        quit()

else:
    print("Enter a valid number")
    quit()

random_number = random.randint(0,top_number)
Track = 0
while True:
    Track += 1
    guess = input("Guesses: ")
    if guess.isdigit():
        guess = int(guess)

        if guess == random_number :
            print("Congratulations you have entered the Exact number!")
            break

        elif guess <= 0:
            print("Please Enter a digit greater than 0")
            continue

    else:
        print("Please enter a valid number!")
        continue
print(f"You have entered {Track} guesses")

