# First step is to declare the correct password
password_correct = "12345"

# Next Step is to use a while loop that can repeatedly ask for the password
while True:
    # Create an input function that asks a user to enter the password
    password_input = input("Enter the password: ")

    # Create a function that checks if the entered password is correct
    if password_input == password_correct:
        print("Access granted!")
    # If the user gets it correct then the break keyword will stop the loop
        break  
    else:
        print("Incorrect password. Please try again.")
