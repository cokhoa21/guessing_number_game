import random

EASY_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 10

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 10")

def check_answer(guess, answer,turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it the answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'difficult', 'easy'")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    answer = random.randint(1,100)

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("Game over.You lose")
            return
        elif guess != answer:
            print("Guess again.")


game()