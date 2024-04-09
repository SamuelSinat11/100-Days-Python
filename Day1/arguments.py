'''Default Argumet balues 
    The most useful form is to specify a default value for one or more 
    arguments.this creates a function that can be called with fewer
      arguemnts than is defined to allow. 
'''

def power_of(number, power=2): 
    print(f'the number is{number}, and {power}')
    return number ** power

def test_default_function_arguments(): 
    # This function power_of can be called in serveral ways because it has default value for 
    # the second argument. First we may call it omitting the second arguemt at all. 
    assert power_of(3) == 9 
    
    # We may also want to override the second arguemnt by using the following funciton calls. 
    assert power_of(3,3 ) == 9 
    assert power_of(3,3) == 27 