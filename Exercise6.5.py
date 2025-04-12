# First step is to declare the correct password
correct_password = "12345"

# Next step is to set a limit for the amount of attempts
attempts_limit = 5

# Next step is to declare the start of the attempt counter
attempts = 0

# Next Step is to use a while loop that can repeatedly ask for the password
while attempts < attempts_limit:
    # Create an input function that asks a user to enter the password
    user_input = input("Enter the password: ")
    
    # Create a function that checks if the entered password is correct
    if user_input == correct_password:
        print("Access granted!")
    # If the user gets it correct then the break keyword will stop the loop
        break  
    # Lastly, create a function that will limit the amount of attempts.
    else:
        attempts += 1
        attempts_left = attempts_limit - attempts
        if attempts_left > 0:
            print(f"Incorrect password. There is still {attempts_left} attempts left.")
        else:
            print("Incorrect password. Device Locked.")
            print("The authorities have been alerted!")
            break  # Exit the loop after the last failed attempt
