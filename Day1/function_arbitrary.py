# Function canbe callled with an arbitrary number of arguments. These arguments will be wrapped up in a tuple. Before the variable 
# number of arguments, zero or more normal arguemnts may occur. 

def test_function_arbitrary_arguments(): 
    
    def test_function(first_param,  *arguments): 
        """This function accepts its arguments through "arguments" tuple"""
        assert first_param == 'first param'
        assert arguments == ('second param', 'thrid param')

    test_function('first param', 'second param', 'third param')

# Normally, these variadic arguments will be last in the list of formal parameters, because 
# they scop up all remaining input arguments that are passed to the function. any formal 

def concat( *args, sep= '/'): 
    return sep.join(args)


assert concat('earth', 'mars', 'venus') == 'earth/mars/venus'
assert concat('earth', 'mars', 'venus', sep='.') == 'earth.mars.venus'


# Normal call withh separate arguments: 
def test(): 
    assert list(range(3,6)) == [3,4,5]

# call with arguments unpacked from a list. 
arguments_list = [3,7]
assert list(range(*arguments_list)) == [3,4,5]

# In the same fashion, dictionaries can deliver keyword arguemnts with the ** operator:
def function_that_receives_names(first_word, second_word): 
    return first_word + ',' + second_word + '!'

argument_dictionary = {'first_word: ': 'Hello', 'second_word': 'world'}
assert function_that_receives_names(**argument_dictionary) == 'Hello, world'


