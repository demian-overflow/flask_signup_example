from settings import AUTH_VALIDATION_EMAIL_PATTERN

from .email import EmailValidator
from .general import LengthValidator
from .utils import validate_string


email_pattern_validator = EmailValidator(AUTH_VALIDATION_EMAIL_PATTERN)
email_length_validator = LengthValidator(min_length=8, max_length=100500)

password_length_validator = LengthValidator(min_length=6, max_length=20)

username_length_validator = LengthValidator(min_length=5, max_length=100)
