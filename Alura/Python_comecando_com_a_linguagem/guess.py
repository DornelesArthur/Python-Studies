print("****************************")
print("Welcome to guess the number!")
print("****************************")

secret_number = 42

try:
    guess = int(input("Guess the number: "))

    print("Your guess is: ", guess)

    correct = secret_number == guess
    higher = secret_number > guess
    if(correct):
        print("You have guess correctly")
    else:
        if (higher):
            print("The secret number is higher than ", guess)
        else:
            print("The secret number is lower than ", guess)

        guess = int(input("You have a second chance. Guess again: "))
        correct = secret_number == guess
        if(correct):
            print("You have guess correctly")
        else:
            print("You have guess wrong")

except ValueError:
    print("Only numbers are accepted!")
