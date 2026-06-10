import random
secret_number= random.randint(1,100)
print("Welcome to Guess the Number! I am thinking of a number between 1 and 100.")
guessed_correct=False
attempts=0
while not guessed_correct:
  guess=int(input("Take a guess: "))
  attempts=attempts+1
  if guess > secret_number:
    print("Too high! Try guessing a lower number")
  elif guess<secret_number:
    print("Too low! try guessing a higher number")
  else:
    print("Congratulations! You guessed the secret number!")
    guessed_correct=True
print("you took",attempts," attempts to guess")
