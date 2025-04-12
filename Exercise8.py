# First step is to declare a variable for the List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Next Step is to declare a variable for the name were searching
name = "Sam"

# Next is using the if function to say that if a name is found then say it was on the list otherwise say it was not on the list
if name in names:
    print(f"{name} is on the list!")
else:
    print(f"{name} is not on the list.")
