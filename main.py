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

import random as rd
options = [rock, paper, scissors]
choice = int(input(" What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
bot_c = rd.randint(0, 2)


if choice >= 3 or choice < 0:
  print("Invalid number, you lose")
else:
  print(options[choice])
  print(f"Computer chose:\n{options[bot_c]}")
  if choice == 0 and bot_c == 2:
    print("You won")
  elif choice == 2 and bot_c == 0:
    print("You lose")
  elif choice > bot_c:
    print("You won")
  elif choice < bot_c:
    print("You lose")
  elif choice == bot_c:
    print("Draw")

 
  
  
  