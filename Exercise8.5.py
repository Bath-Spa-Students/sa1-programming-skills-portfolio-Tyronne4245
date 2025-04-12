# First step is to declare a variable for the List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Next Step is to declare a variable for the name were searching
name = input("Enter the name you are searching for on the list: ")

# Next step is to create an if function that says 'is on the list' if your input is on the list otherwise it will say not on the list if not on the list
if name in names:
    print(f"{name} is on the list!")
else:
    print(f"{name} is not on the list.")
