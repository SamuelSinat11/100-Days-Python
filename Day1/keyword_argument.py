
import pytest 

def parrot(voltage, state="a stiff", action= 'voom', parrot_tpye="Norwegian Blue"): 
    # This function accepts one required argument(voltage) and three optional arguments 
    # (state, action, and type). 
    
    message = "this parrot would" + action + ''
    message += 'if you put' + str(voltage) + 'volts through it.'
    message += 'Lovely plumage , the ' + parrot_tpye + '.'
    message += 'It\s' + state + '!'

    return message

def test_function_keyword_arguments(): 
    
    message = ( 
         "This parrot wouldn't voom if your put 10000 volts through it."
         "Lovely plumage, the Norwegian Blue."
         "it's a stiff!"
    )
    # 1 positional argument 
    assert parrot(1000) == message 
    # 2 keyword argument 
    assert parrot(voltage=1000) == message 
    
    message = (
        "this parrot wouldn't VOOOOM if you put 100000 volts through it."
        "Lovely plumage, the Norwegian Blue"
        "It's a stiff"
    )


    