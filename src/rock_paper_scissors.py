import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

hands = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(hands[user_choice])

computer_choice = random.randint(0, 3)

print("Computer chose:")

print(hands[computer_choice])

if user_choice == computer_choice: # Tie
    print("You tie")

if user_choice == 0: # Rock
    if computer_choice == 1: # Paper
        print("You lose")
    else: # Scissors
        print("You win")
elif user_choice == 1: # Paper
    if computer_choice == 0: # Rock
        print("You win")
    else: # Scissors
        print("You lose")
else: # Scissors
    if computer_choice == 0: # Rock
        print("You lose")
    else: # Paper
        print("You win")





