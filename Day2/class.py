
# python is an object oriented programming language. 
# Almost everything in python is an object, with its properties and methods. 
# A class is like an object cconstructor, or a "blueprint" for creating object. 

class GreetingClass: 
    def __init__(self, name='user'):
        self.name = name

    def say_hello(self): 
        return 'Hello ' + self.name 
    
    def say_goodbye(self): 
        return 'Goodbye ' + self.name 

# Creating an instance of the GreetingClass
greeter = GreetingClass()

# Testing the methods
assert greeter.say_hello() == "Hello user"
assert greeter.say_goodbye() == "Goodbye user"  