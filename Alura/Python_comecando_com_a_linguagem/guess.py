import random as r
print("****************************")
print("Welcome to guess the number!")
print("****************************")

secret_number = r.randrange(1,100)
number_chances = 4

try:
    while (number_chances):
        guess = int(input(f"Guess the number ({number_chances} chances left): "))

        print("Your guess is: ", guess)

        correct = secret_number == guess
        higher = secret_number > guess
        if(correct):
            print("You have guess correctly")
            number_chances = 0
        else:
            if (higher):
                print("The secret number is higher than ", guess)
            else:
                print("The secret number is lower than ", guess)
            number_chances-=1
    print("Game has ended")
    print(f"The right number was: {secret_number}")
except ValueError:
    print("Only numbers are accepted!")
