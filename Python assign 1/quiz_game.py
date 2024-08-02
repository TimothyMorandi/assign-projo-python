print("Welcome to this quiz game")
play = input("Do you want to play (yes/no)? ").lower()
if play != "yes":
    quit()
print("Okay! Let's do it:)")
score = 0

answers = input("What does 'CPU' stand for? ").lower()
if answers == "central processing unit":  # Corrected to lowercase comparison
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("next>>")

answers = input("What does 'GPU' stand for? ").lower()
if answers == "graphics processing unit":  # Corrected to lowercase comparison
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("next>>")

answers = input("What does 'RAM' stand for? ").lower()
if answers == "random access memory":  # Corrected to lowercase comparison
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("next>>")

answers = input("What does 'ROM' stand for? ").lower()
if answers == "read only memory":  # Corrected to lowercase comparison
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("Your got " + str(score) + " correct")
print("You got " + str((score/4)*100) + "%")