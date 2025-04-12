# First Step is to write a function that checks if a number is even or odd
def Even_Or_Odd(num):
    if num % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

# Next Step is to create a function that will run when its called
def main():
    # Next Step is to ask a number from a user
    user_input = int(input("Please enter a number: "))
    
    # Next Step is to pass the inputted number to the Even_Or_Odd function
    result = Even_Or_Odd(user_input)
    
    # Next Step is to print the message that the function returned
    print(result)

# Lastly is to call the main function
if __name__ == "__main__":
    main()
