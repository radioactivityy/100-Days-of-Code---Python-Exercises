import random

# Input string containing names separated by commas and spaces
names_string = "Angela, Ben, Jenny, Michael, Chloe"

# Split the string into a list using the comma and space as delimiters
names = names_string.split(", ")

# Generate a random index to select a name from the list
random_index = random.randint(0, len(names) - 1)

# Select the random name using the generated index
selected_name = names[random_index]

# Print the message with the randomly chosen name
print(f"{selected_name} is going to buy the meal today!")
