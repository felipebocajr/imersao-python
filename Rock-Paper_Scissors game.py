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

import random
rock_play = "\n\ncomputer choose:\n\n" + rock + "\n\n"
paper_play = "\n\ncomputer choose:\n\n" + paper + "\n\n"
scissors_play = "\n\ncomputer choose:\n\n" + scissors + "\n\n"
random_play = random.randint(1,3)
player_choice = input("Welcome to the Rock Paper Scissors game! Make your move.\nType 1 for Rock, 2 for Paper and 3 for Scissors.\n")
if player_choice == "1":
  print("\nyou choose:\n\n" + rock)
  if random_play == 1:
    print(rock_play + "draw")
  elif random_play == 2:
    print(paper_play + "you lost")
  else:
    print(scissors_play + "you win")
elif player_choice == "2":
  print("\nyou choose:\n\n" + paper)
  if random_play == 1:
    print(rock_play + "you win")
  elif random_play == 2:
    print(paper_play + "draw")
  else:
    print(scissors_play + "you lost")
elif player_choice == "3":
  print("\nyou choose:\n\n" + scissors)
  if random_play == 1:
    print(rock_play + "you lost")
  elif random_play == 2:
    print(paper_play + "you win")
  else:
    print(scissors_play + "draw")
else:
  print("invalid answer, type a valid number.")
