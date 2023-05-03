import random
import message_gpt

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
options = ["rock", "paper", "scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(hands[user_choice])

computer_choice = random.randint(0, 3)

print("Computer chose:")

print(hands[computer_choice])

print(message_gpt.gen_message(options[user_choice], options[computer_choice]))




