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

# Write your code below this line 👇
import random

game = [rock, paper, scissors]
user = input("Your chose 0, 1, or 2\n")
your_chose = game[int(user)]
print(your_chose)

computer_ran = random.randint(0, 2)
computer_chose = game[computer_ran]
print("Computer chose:" + computer_chose)

if your_chose == rock:
    if computer_chose == rock:
        print("draw")
    elif computer_chose == scissors:
        print("You win")
    else:
        print("You lose")


elif your_chose == scissors:
    if computer_chose == scissors:
        print("draw")
    elif computer_chose == paper:
        print("You win")
    else:
        print("You lose")

else:
    if computer_chose == paper:
        print("draw")
    elif computer_chose == rock:
        print("You win")
    else:
        print("You lose")