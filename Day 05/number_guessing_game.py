print("=== Number Guessing Game ===\n")

secret = 12
attempts = 0
max_attempts = 5

while(1):

    #check attempts
    if attempts >= max_attempts:

        print("You lost! The number was", secret)
        break

    guess = int(input("Enter your guess : "))
    attempts += 1

    print("") #used for a new line

    #check guess
    if guess == secret:

        print("Correct! You won.")
        break

    elif guess < secret:

        print("Too low.")

    else:

        print("Too high.")

    #show remaining
    left = max_attempts - attempts

    if left > 0:

        print("Attempts left :", left)

    else:

        pass
