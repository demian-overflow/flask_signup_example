from bcrypt import hashpw, checkpw, gensalt

from .abc import AbstractPasswordHashingStrategy


class BCryptPasswordHashingStrategy(AbstractPasswordHashingStrategy):
    def __init__(self, salt_size: int):
        self.salt_size = salt_size

    def hash_password(self, password: str) -> str:
        return (
            hashpw(password.encode(), gensalt(rounds=self.salt_size))
        ).decode()

    def verify_password(self, password: str, hashed: str) -> bool:
        return checkpw(password.encode(), hashed.encode())
