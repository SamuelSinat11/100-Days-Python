
def greet(name): 

    def get_message(): 
        return "Hello I am is "
    result = get_message() + name 
    return result
 
greet_someone = greet
print(greet_someone("Jonh"))


def Employee(name): 
    return "Hello My name is " + name 

def call_func(func): 
    other_name = "Samuel"
    return func(other_name)

print(call_func(Employee))


def compose_greet_func(name): 
    def get_message(): 
        return "hello there " + name + "!"
    return get_message

greet = compose_greet_func("Sammy")
print(greet())


def get_text(name): 
    return "My name is, {0} I'm from cambodia". format(name)

def p_decorate(func): 
    def func_wrapper(name): 
        return "<p> {0} </p>". format(func(name))
    return func_wrapper

my_get_text = p_decorate(get_text)
print(my_get_text("John wick"))


print ("==============")

def p_decorate(func): 
    def func_wrapper(name):
        return "<p> {0} <p> ". format(func(name))
    return func_wrapper

@p_decorate
def get_text(name): 
    return "I'm a software developer from {0}". format(name)

print(get_text("Norton"))


print ("==============")

def Y_decorate(func): 
    def func_wrapper(name): 
        return "<p> {0} <p> ".format(func(name))
    return func_wrapper

def strong_decorate(func): 
    def func_wrapper(name): 
        return "<strong> {0} </strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name): 
        return "<div> {0} </div>".format(func(name))
    return func_wrapper

@div_decorate
@Y_decorate
@strong_decorate

def get_text(name): 
    return "Our experice I have studies {0} for two years to become expert".format(name)

print(get_text("Python"))


# Decorating Methods 

def v_decorate(func): 
    def func_wrapper(self): 
        return "<p> {0}<p> ".format(func(self))
    return func_wrapper

class identity(object):
    def __init__(self): 
        self.name = "Samuel"
        self.family = "Sinat"

    @v_decorate
    def get_fullname(self): 
        return self.name + " " + self.family
    
my_person = identity()
print(my_person.get_fullname())



