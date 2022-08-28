import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
game_mode = ''

while game_mode != 'easy' and game_mode != 'hard':
    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
life = 11 if game_mode == 'easy' else 5

generate_number = random.choice(range(1, 101))
#print(generate_number)


def check_number(lifes, guess_num) :
  if generate_number == guess_num :
    lifes = -1
    print("right answer!")
    return lifes
  elif generate_number < guess_num :
    lifes -= 1
    print("Too high.\nGuess again.")
    return lifes
  else:
    lifes -= 1
    print("Too low.\nGuess again.")
    return lifes

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
game_mode = ''

while game_mode != 'easy' and game_mode != 'hard':
    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
life = 11 if game_mode == 'easy' else 5

generate_number = random.choice(range(1, 101))
while life > 0 :
  guess = int(input("Make a guess :"))
  life = check_number(life, guess)
  if life > 0:
    print(f"You have {life} attempts remaining to guess the number.")

if life == 0:
  print("You've run out of guesses, you lose")
else:
  print("You win")
