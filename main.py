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

yourChoice = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors. "))

computerChoice = random.randint(0,2)



if yourChoice == computerChoice:
  print(option[yourChoice])
  print("Computer chose:")
  print(option[computerChoice])
  print("Draw")
elif yourChoice == 0 and computerChoice == 2:
  print(option[yourChoice])
  print("Computer chose:")
  print(option[computerChoice])
  print("You win!")
elif yourChoice == 0 and computerChoice == 1:
  print(option[yourChoice])
  print("Computer chose:")
  print(option[computerChoice])
  print("You lose!")
elif yourChoice == 1 and computerChoice == 0:
  print(option[yourChoice])
  print("Computer chose:")
  print(option[computerChoice])
  print("You win!")
elif yourChoice == 1 and computerChoice == 2:
  print(option[yourChoice])
  print("Computer chose:")
  print(option[computerChoice])
  print("You lose!")
elif yourChoice == 2 and computerChoice == 0:
  print(option[yourChoice])
  print("Computer chose:")
  print(option[computerChoice])
  print("You lose!")
elif yourChoice == 2 and computerChoice == 1:
  print(option[yourChoice])
  print("Computer chose:")
  print(option[computerChoice])
  print("You win!")
else:
  print("Error")
