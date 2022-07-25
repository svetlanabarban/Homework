
#Assignment
import random
random_number = random.randint(0, 50)

for attempt in range(7):
    user_guess = int(input("Guess number: "))

    #"The value is too low" if the guessed number less than random generated
    #"The value is too high" if the guessed number higher than random generated
    #"You guessed correctly" if the number is right

    if user_guess < random_number:
        print("The value {} is too low")
    elif user_guess > random_number:
        print("The value is too high")
    elif user_guess == random_number:
        print("You guessed correctly")
        break



