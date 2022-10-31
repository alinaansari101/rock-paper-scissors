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

def get_art(input):
  if input == 0:
    print(rock)
  elif input == 1:
    print(paper)
  elif input == 2:
    print(scissors)

  
my_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
computer_output = random.randint(0, 2)

# ART
get_art(my_input)
print("Computer chose:\n")
get_art(computer_output)


if my_input == computer_output:
  print("Draw")

if (my_input == 0 and computer_output == 1) or (my_input == 1 and computer_output == 2) or (my_input == 2 and computer_output == 0):
  print("You lose")

if (my_input == 1 and computer_output == 0) or (my_input == 2 and computer_output == 1) or (my_input == 0 and computer_output == 2):
  print("You Win")
  


