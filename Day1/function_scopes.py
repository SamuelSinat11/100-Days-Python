
def test_function_scopes(): 
    """Scopes and Namespaces Example"""
    # This is an example demonstrating how to reference the different scpes and namespaces, and 
    # how globle and cnonlocal affect variable binding:
     
    # pylint: disable= redefined-outer-name 
    test_variable = 'initial value inside test function'

    def do_local(): 
        #Create variable that is only accessible inside current do_local() functions. 
        # pylint: disable = redefined-outer-name 
        test_variable = 'local value'
        return test_variable
    
    def do_nonlocal(): 
        # Address the variable from outer scope and try to change it. 
        # pylint: disable = redefined-outer-name 
        nonlocal test_variable
        test_variable = 'nonlocal value'
        return test_variable 
    
    def do_global(): 
        # Address the variable from very global scope and try to change it. 
        # pylint: disble = redefined-outer-name, global-statement 
        global test_variable 
        test_variable = 'global value'
        return test_variable 
    

# on this level cureently we have access to local for test_function_scopes() function variable. 
assert test_variable == 'initial value inside test function'

# Do local assigment 
# It doesn't change global varialbe and variable from test_function() scope. c
do_local()
assert test_variable == 'initial value inside test function'

# Do non local assignment 
do_nonlocal()
assert test_variable == 'nonlocal value'

do_global()
assert test_variable == 'nonlocal value'



