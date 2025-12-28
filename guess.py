import random

print(" Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 50.")

number = random.randint(1, 50)
guess = None
attempts = 0

while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again ")
    elif guess > number:
        print("Too high! Try again ")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
