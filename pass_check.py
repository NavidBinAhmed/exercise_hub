def is_strong_pass(password):
    '''checks if a given password is strong or weak'''

    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True

## calling function
password_1 = 'WeakPwd'
result_1 = is_strong_pass(password_1)
print(result_1) # output: False

password_2 = 'WeakPwd1_^'
result_2 = is_strong_pass(password_2)
print(result_2) # output: True