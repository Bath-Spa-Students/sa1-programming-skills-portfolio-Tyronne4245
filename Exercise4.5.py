# First step is to create a list of the countries and their capitals
quiz = {
    "United Kingdom": "London",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Netherlands": "Amsterdam",
    "Greece": "Athens",
    "Denmark": "Copenhagen",
    "Hungary": "Budapest",
    "Ireland": "Dublin",
    "Sweden": "Stockholm",
    "France": "Paris"
}

# Next step is to create a function that will run the quiz
def QuizTest():
    correct_answers = 0

    # Create a function that will allow each country in the quiz by using the for function
    for country, capital in quiz.items():
        # Create a function that will allow a user to input their answer
        # The strip() method removes any leading, and trailing whitespaces.
        # The lower() method returns a string where all characters are lower case.
        user_input = input(f"What is the capital of {country}? ").strip().lower()

        # Create another function that checks if the answer is correct or not by using the if function
        if user_input == capital.lower():
            print(f"Your Answer is Correct!. The capital of {country} is {capital}.")
            correct_answers += 1
        else:
            print(f"Your Answer is Wrong!. The capital of {country} is {capital}.")

    # Final score
    print(f"\nYou scored {correct_answers} out of {len(quiz)}")
    if correct_answers >= 5:
        print("Good Job!")
    else:
        print("Better Luck Next Time")

# Run the quiz
QuizTest()
