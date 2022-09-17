# from venv import create

import time
from logging_dec import create_logger, dec_calc_time, dec_exception, dec_profile
from MyException import (BaseValidationError, NotGoodError,
                         PasswordTooAnnoy, PasswordTooLong, PasswordTooShort, TooBadError)

my_logger = create_logger()


def validate(password: str):
    if len(password) < 4:
        raise PasswordTooShort(f'password too short: {password}')
    elif len(password) > 8:
        raise PasswordTooLong(f'password too long: {password}')
    elif 'qq' in password:
        raise PasswordTooAnnoy(f'password too annoy: {password}')
    else:
        print("Ur password is strong enough")


def check_exception(input_value: int):
    if input_value > 0:
        print(f"Input is okay: {input_value} ")
    elif input_value < 0 and input_value >= -1000:
        raise NotGoodError(f"You have input a negative value {input_value}")
    else:
        raise TooBadError(f"You have input a very small value {input_value}")


@dec_exception(my_logger)
@dec_calc_time(my_logger)
def run_exception(input_value: int):
    check_exception(input_value)


@dec_profile(my_logger)
def main():
    my_logger.info("U are visiting main()")
    time.sleep(3)
    try:
        validate("1234")
    except BaseValidationError as err:
        my_logger.info(f"here: {str(err)}")
        raise


if __name__ == "__main__":
    print("--- Execute ---")
    main()
    run_exception(input_value=99999)
    print("--- Done ---")
