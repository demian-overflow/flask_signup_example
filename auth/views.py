from .base import BaseFormSignup
from .validators import email_length_validator, email_pattern_validator
from .validators import username_length_validator
from .validators import password_length_validator


class FormSignupWithoutVerification(BaseFormSignup):
    email_verification_enabled = False

    username_validators = [username_length_validator]
    email_validators = [email_length_validator, email_pattern_validator]
    password_validators = [password_length_validator]
