import random

def generate_game(random_number, guess_number):
    number = None
    while number != random_number:
        number = int(input("Guess the random number: "))
        guess_number += 1
        if random_number > number:
            print("Too low!")
        elif random_number < number:
            print("Too high!")
    
    print(f"Congratulations! You've guessed the number in {guess_number} attempts.")
    return 

print("""
Welcome to the Number Guessing Game!
Try to guess the number between 1 and 100.
""")

guess_number = 0
random_number = random.randint(1, 100)
print("The random number has been generated (for testing purposes):", random_number)
generate_game(random_number, guess_number)
