from venv import create

from logging_dec import create_logger, exception


class BaseValidationError(ValueError):
    pass

class PasswordTooShort(BaseValidationError):
    pass

class PasswordTooLong(BaseValidationError):
    pass

class PasswordTooAnnoy(BaseValidationError):
    pass

class NotGoodError(Exception):
    pass

class TooBadError(Exception):
    pass

def validate(password:str):
    if len(password)<4:
        raise PasswordTooShort(f'password too short: {password}')
    elif len(password)>8:
        raise PasswordTooLong(f'password too long: {password}')
    elif 'qq' in password:
        raise PasswordTooAnnoy(f'password too annoy: {password}')
    else:
        print("Ur password is strong enough")

def check_exception(input_value:int):
    if input_value > 0:
        print(f"Input is okay: {input_value} ")
    elif input_value < 0 and input_value >= -1000:
        raise NotGoodError(f"You have input a negative value {input_value}") 
    else:        
        raise TooBadError(f"You have input a very small value {input_value}") 

@exception(create_logger())
def run_exception(input_value:int):
    check_exception(input_value)

def main():
    print("Hello")
    try:
        validate("abcqqq")
    except BaseValidationError as err:
        print(err)
    # print("Another approach...")
    # validate("aa")

if __name__=="__main__":
    print("--- Execute ---")
    # main()
    run_exception(input_value=-9)
    print("Bye bye...")
