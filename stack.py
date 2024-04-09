def greet2(name):
    print(f"how are you, {name}?")
    
def bye():
    print("Okay, bye!")

def greet1(name):
    print(f"Hello {name} !")
    greet2(name)
    print(f"Getting ready to say bye")
    bye()

# Call greet1 function with an argument
greet1("Alice")

# The variable name set to Alice, that needs to be saved in memory. Every time you make a function call, 
# your computer saves the values for all the variables for that memory call in memory.
#  Greet 1
# Name: Alice
# Greet 2
# Name: Alice
# Bye