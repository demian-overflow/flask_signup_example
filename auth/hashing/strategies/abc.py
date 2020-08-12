from abc import ABC


class AbstractPasswordHashingStrategy(ABC):
    def hash_password(self, password: str) -> str:
        raise NotImplementedError

    def verify_password(self, password: str, hashed: str) -> bool:
        raise NotImplementedError
