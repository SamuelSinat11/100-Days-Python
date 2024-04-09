
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


# Functions can return other functions. In other words, functions generating other functions 

def compose_greet_func(): 
    def get_message(): 
        return 'Hello there!'
    
    return get_message 

greet_function = compose_greet_func()
assert greet_function() == 'Hello there!'


# Inner functions have access to the enclosing scope. 

# More commonly know as a closure. A very powerful pattern that we will come across while 
# building decorators. Another thing to note, python only allows read access to the outer 
# scope and not assigment. Notice how we modified the example above to read a "name" argument 
# from the enclosing scope of the inner function and return the new function. 

def compose_greet_func_with_closure(name): 
    def get_message(): 
        return "Hello" + name + "!"

    return get_message

greet_with_closure = compose_greet_func_with_closure("Jonh")
assert greet_with_closure() == "Hello there, Jonh! "

