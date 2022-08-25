import random
import string
import os


PASSWORD_MIN_LENGTH = 4
PASSWORD_MAX_LENGTH = 30
 
 
settings ={
    'lower' : True,
    'upper': True,
    'symbol' : True,
    'number' : True,
    'space' : False,
    'length' : 8
    }

def clear_screen():
    os.system('cls')
    
        
def get_user_password_length(option, default, pw_min_length=PASSWORD_MIN_LENGTH, pw_max_length=PASSWORD_MAX_LENGTH):
    while True:
        user_input = input('Enter your passworg length. '
                           f'(Default is {default})'
                           '(enter : default): ')
        
        if user_input == '':
            return default
        
        if user_input.isdigit():
            user_password_length = int(user_input)
            if pw_min_length <= user_password_length <= pw_max_length:
                return user_password_length
            print(f'Please enter a number between {pw_min_length} and {pw_max_length}.')
        else:       
            print('Invalid input.Please enter a Number.')
            
        print('Please try again')
            
            
def get_yes_or_no_for_settings(option, default):
    while True:
        user_input = input(f'Include {option}? '
                           f'(Default is {default}) '
                           '(y: yes, n: no, enter: default): ')
        
        if user_input == '':
            return default
        
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print('Invalid input. please enter y or n.')
 
 
def set_settings(settings):

    for option, default in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no_for_settings(option, default)
            settings[option] = user_choice
        else:
            user_password_length = get_user_password_length(option, default)
            settings[option] = user_password_length


def ask_if_change_settings(settings):
    while True:
        user_answer = input('Do you want to change Defaule settings generator?'
                            '(y:yes, n:no, enter:yes): ')
        print('-'*20, 'Change Settings', '-'*20)
        
        if user_answer in ['y', 'n', '']:
            if user_answer in ['y', '']:
                set_settings(settings)
            break
        else:
            print('Invalid input.Please enter (y:yes, n:no, enter:yes).')
        
      
def get_random_upper_case():
    return random.choice(string.ascii_uppercase)


def get_random_lower_case():
    return random.choice(string.ascii_lowercase)


def get_random_number():
    return random.choice("0123456789")


def get_random_symbol():
    return random.choice("""~!@#$%^&*(/)–_=+["]{|}<\>?""")


def generate_random_char(choices):
    choice = random.choice(choices)
    
    if choice == 'upper':
        return get_random_upper_case()
    if choice == 'lower':
        return get_random_lower_case()
    if choice == 'number':
        return get_random_number()
    if choice == 'symbol':
        return get_random_symbol()
    if choice == 'space':
        return ' '


def password_generator(settings):
    final_password = ''
    password_length = settings['length']

    choices = list(filter(lambda x: settings[x], ['upper', 'lower', 'symbol', 'space', 'number']))
    
    for i in range(password_length):
        final_password += generate_random_char(choices)
    
    return final_password
    

def ask_user_another_password():
    while True:
        print('-'*20)
        user_answer = input('Regenerate another password? (y: yes, n: no, enter:yes): ')
        if user_answer in ['y', 'n', '']:
                if user_answer == 'n':
                    return False
                return True
        else:
            print('Invalid input, Please enter (y: yes, n: no, enter:yes).')
            
                    
def password_generator_loop(settings):
    while True:
        print('-'*20)
        print(f'Your Random Password: {password_generator(settings)}')
        
        if ask_user_another_password() == False:
            break
            
    
def run():    
    clear_screen()   
    ask_if_change_settings(settings)
    password_generator_loop(settings)
    print('Thank you for choosing us.')


run()