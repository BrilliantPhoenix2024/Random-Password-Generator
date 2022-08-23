

from distutils.sysconfig import get_python_inc
from optparse import Option


settings ={
    'lower' : True,
    'upper': True,
    'symbol' : True,
    'number' : True,
    'space' : False,
    'length' : 8
    }


def get_yes_or_no_for_settings(option, default):
    while True:
        user_input = input(f'Include {option}? (Default is {default}) (y: yes, n: no): ')
        
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print('Invalid input. please enter y or n.')
 
 
