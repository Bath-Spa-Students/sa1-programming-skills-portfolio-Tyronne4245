# First step is to define a dictionary with month numbers as keys and the number of days as values
month_days = {
    1: 31,   
    2: 28,   
    3: 31,   
    4: 30,   
    5: 31,   
    6: 30,   
    7: 31,   
    8: 31,   
    9: 30,   
    10: 31,  
    11: 30,  
    12: 31   
}

def is_leap_year():
    leap_year_answer = input("Is it a Leap Year Today?:").strip().lower()
    return leap_year_answer == "yes"

# Next Step is to allow input for a user for a month number (1-12)
month_num = int(input("Enter a months number (Example: January=1, February=2): "))

# Next Step is to create a function to check if the input is a valid number and within the range of 1 to 12 by using the if function
# Month 2 will have extra conditions to fulfill to know if it is a leap year or not 
if 1 <= month_num <= 12:
    if month_num == 2:
        if is_leap_year():
            print(f"Their are 29 days in month {month_num} during a leap year")
        else:
            print(f"Their are 28 days in month {month_num} outside a leap year")
    else:
        print(f"Their are {month_days[month_num]} days in month {month_num}")
else:
    print("Invalid Input! Please enter a number between 1 and 12.")


