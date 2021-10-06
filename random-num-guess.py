import random

def play_game():
  number = random.randint(1, 101)
  lives = 0
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("'easy' or 'hard': ").lower()
  if difficulty == "easy":
    lives += 10
  if difficulty == "hard":
    lives += 5

  guess_is_incorrect = True
  while guess_is_incorrect and lives > 0:
    if difficulty == "easy":
      print(f"You have {lives} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if guess == number:
        print("You got it!")
      elif guess > number:
        print("Too high.")
        lives -= 1
      elif guess < number:
        print("Too low")
        lives -= 1
    if difficulty == "hard":
      print(f"You have {lives} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if guess == number:
        print("You got it!")
      elif guess > number:
        print("Too high.")
        lives -= 1
      elif guess < number:
        print("Too low")
        lives -= 1
  if lives == 0:
    print("You ran out of lives!")
    
play_game()
