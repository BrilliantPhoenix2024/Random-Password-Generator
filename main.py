 

settings ={
    'lower' : True,
    'upper': True,
    'symbol' : True,
    'number' : True,
    'space' : False,
    'length' : 8
    }


def get_user_password_length(option, default, pw_min_length=4, pw_max_length=30):
    while True:
        user_input = input(f'Enter your passworg length. (Default is {default}) (enter : default): ')
        
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
        user_input = input(f'Include {option}? (Default is {default}) (y: yes, n: no, enter: default): ')
        
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


set_settings(settings)