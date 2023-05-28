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
