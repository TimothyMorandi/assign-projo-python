import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Rock/Paper/Scissors or Q to Quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)  # Random number between 0 and 2
    computer_pick = options[random_number]
    print(f"Computer pick is {computer_pick}:")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1

    else:
        print("The Computer wins and this means you lost!")
        computer_wins += 1

print(f"User result is {user_wins}.")
print(f"Computer result is {computer_wins}.")
print("Byee")