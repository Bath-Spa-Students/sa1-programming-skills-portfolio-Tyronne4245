# First Step is to create a function that allows user to input their name, hometown, and age
name = input("Enter your full name: ")  
hometown = input("Enter your hometown: ")

# Next step is to use some functions for the age input to ensure it is a valid number by looping with the try and except block
while True:
    input_age = input("Enter your age: ")
    
    try:
        age = int(input_age)  
    # The Break Keyword allows for the loop to stop if the input follows the conditions
        break  
    except:
        print("Invalid Input. Please enter a number for age.")

# Next Step is to create a dictionary to store data values in key:value pairs.
information = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Next step is to print the values on separate lines with only one print function
print(f"\nName: {information['name']}\nHometown: {information['hometown']}\nAge: {information['age']}")
