print("****************************")
print("Welcome to guess the number!")
print("****************************")

secret_number = 42

try:
    guess = int(input("Guess the number: "))

    print("Your guess is: ", guess)

    if(secret_number == guess):
        print("You have guess correctly")
    else:
        print("You have guess wrong")
except ValueError:
    print("Only numbers are accepted!")
