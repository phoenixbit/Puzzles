# code to implement the guessing game in python
import random


def value_generator():
    return random.randint(0, 200)


def guessing_game(generated_value, user_input, i):
    if user_input == generated_value:
        print("CONGRATS!!!! YOU FOUND THE ANSWER!! THE ANSWER WAS : " + str(generated_value) + " AND YOU GUESSED IT IN ATTEMPT " + str(i))
        exit(0)
    while user_input > generated_value:
        print("Guess lower")
        user_input = int(input("Input next guess : "))
        i += 1
        guessing_game(generated_value, user_input, i)
    while user_input < generated_value:
        print("Guess higher")
        user_input = int(input("Input next guess : "))
        i += 1
        guessing_game(generated_value, user_input, i)


if __name__ == '__main__':
    inputted_value = int(input("Input guess 1 : "))
    i = 2
    generated_number = value_generator()
    guessing_game(generated_number, inputted_value, i)
