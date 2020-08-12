from re import fullmatch

from .abc import AbstractValidator


class EmailValidator(AbstractValidator):
    def __init__(self, email_pattern: str):
        self.email_pattern = email_pattern

    def valid(self, email: str) -> bool:
        match = fullmatch(self.email_pattern, email)

        return match is not None
