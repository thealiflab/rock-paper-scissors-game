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

option = [rock, paper, scissors]

yourChoice = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n"))
if yourChoice >=3 or yourChoice <0:
  print("You typed an invalid input, You lose!")
  exit()
print(option[yourChoice])

computerChoice = random.randint(0,2)
print("Computer chose:")
print(option[computerChoice])

if yourChoice == computerChoice:
  print("Draw")
elif yourChoice == 0 and computerChoice == 2:
  print("You win!")
elif yourChoice == 0 and computerChoice == 1:
  print("You lose!")
elif yourChoice == 1 and computerChoice == 0:
  print("You win!")
elif yourChoice == 1 and computerChoice == 2:
  print("You lose!")
elif yourChoice == 2 and computerChoice == 0:
  print("You lose!")
elif yourChoice == 2 and computerChoice == 1:
  print("You win!")
else:
  print("Error")
