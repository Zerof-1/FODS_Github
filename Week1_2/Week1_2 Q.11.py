import random

# I. Generate a random number between 1 and 100
answer = random.randint(1, 100)

# II. Allow up to 5 guesses
max_attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100. You have 5 tries.")

# III. Loop through user guesses
for attempt in range(1, max_attempts + 1):
    try:
        guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))

        if guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")
        else:
            print(f"Correct! The number was {answer}. You guessed it in {attempt} tries.")
            break  # Exit the loop if guessed correctly
    except ValueError:
        print("Invalid input! Please enter a number.")

else:
    # V. If loop completes without break
    print(f"\nGame Over! The correct number was {answer}.")




