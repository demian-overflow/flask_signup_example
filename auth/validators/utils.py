from .abc import AbstractValidator


def validate_string(string: str, validators: [AbstractValidator]) -> bool:
    for validator in validators:
        if not validator.valid(string):
            return False

    return True
