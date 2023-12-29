import random

min_number = 1
max_number = 100
num_guesses = 5

guess = random.randint(min_number, max_number)

for i in range(num_guesses):
    response = input(f"My guess is {guess}. Is it High, Low, or Correct? ").lower()

    if response == "high":
        max_number = guess - 1
    elif response == "low":
        min_number = guess + 1
    elif response == "correct":
        print("Yay! I guessed it!")
        break

    guess = random.randint(min_number, max_number)

else:
    print("Aww, I couldn't guess it in time.")