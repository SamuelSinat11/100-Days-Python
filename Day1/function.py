
# Assign functions to variable 

def greet(name): 
    return "Hello," + name 

greet_someone = greet 

assert greet_someone("Jonh") == "Hello, Jonh"

# Define functions inside other functions. 

def greet_again(name): 
    def get_message():
        return "Hello," 
    result = get_message() + name 
    return result

assert greet_again("Jonh") == "Hello, Jonh"