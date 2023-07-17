#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
print(logo)
# Allow the player to submit a guess for a number between 1 and 100.
import random
answer = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {answer}")

is_game_over = False
difficulty = {
  'easy': 10,
  'hard': 5
}

difficulty_selection = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_selection in difficulty:
  value = difficulty[difficulty_selection]
  print(f"You have {value} attempts remaining to guess the answer.")

attempts = value

while not is_game_over:
  guess = int(input("Make a guess. "))
  

  if guess == answer:
    is_game_over = True
    print(f"You got it! Answer was {answer}")
  elif guess > answer:
    attempts -= 1
    if attempts == 0:
      is_game_over = True
      print("Too high.")
      print("You've run out of guesses. You lose.")
    else:
      print("Too high.")
      print("Guess again.")
      print(f"You have {attempts} attempts remaining to guess the answer.")
  elif guess < answer:
    attempts -= 1
    if attempts == 0:
      is_game_over = True
      print("Too low.")
      print("You've run out of guesses. You lose.")
    else:
      print("Too low.")
      print("Guess again.")
      print(f"You have {attempts} attempts remaining to guess the answer.")
  
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

