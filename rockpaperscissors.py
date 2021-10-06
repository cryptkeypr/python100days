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


choice = input("What do you choose? Type 0 for Rock, 1 for paper or 2 Scissors.\n")
pc_choice = round(random.randint(0, 2), 0)

if choice == "0":
  print(rock)
  print(f"\nComputer chose:{pc_choice}\n")
  if pc_choice == 1:
    print(paper)
    print("You lose.")
  elif pc_choice == 0:
    print(rock)
    print("It's a draw.")
  else:
    print(scissors)
    print("You win!")
elif choice == "1":
  print(paper)
  print(f"\nComputer chose:\n{pc_choice}")
  if pc_choice == 1:
    print(paper)
    print("It's a draw..")
  elif pc_choice == 0:
    print(rock)
    print("You win!")
  else:
    print(scissors)
    print("You lose.")
elif choice == "2":
  print(scissors)
  print(f"\nComputer chose:\n{pc_choice}")
  if pc_choice == 1:
    print(paper)
    print("You win!")
  elif pc_choice == 0:
    print(rock)
    print("You lose.")
  else:
    print(scissors)
    print("It's a draw.")
else:
  print("Not a valid choice.") 
