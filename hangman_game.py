import random

words = ["python", "computer", "game", "coding"]
word = random.choice(words)

guesses = ""
chances = 6

print("Welcome to Hangman!")

while chances > 0:
    failed = 0

    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()

    if failed == 0:
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()
    guesses += guess

    if guess not in word:
        chances -= 1
        print("Wrong! You have", chances, "chances left.")

        if chances == 0:
            print("You lost! The word was:", word)
