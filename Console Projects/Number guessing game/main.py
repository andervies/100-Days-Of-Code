# todo: import random.int, logo
from random import randint

# todo: print logo
print("Welcome! I am thinking of a number between 1 and 100")
# todo: ask for difficulty and initialize attempts
def difficulty():
    level = input("type 'easy' or 'hard' ")
    if level == "easy":
        return EASY
    elif level == "hard":
        return HARD
    else:
        return "your response is invalid. please type either 'easy' or 'hard'"


EASY = 10
HARD = 5
answer = randint(1, 100)
print(answer)
attempts = difficulty()

while attempts != 0:
    print(f"you have {attempts} attempts left")
    guess = int(input("make a guess: "))
    # todo: check wether guess = answer
    def checker(guess, answer, attempts):
        if guess == answer:
            print("congrats, you got it right")
        elif guess > answer:
            print("too high.")
            return attempts - 1
        else:
            print("too low.")
            return attempts - 1


    attempts = checker(guess, answer, attempts)







# todo: loop game until attempts = 0









