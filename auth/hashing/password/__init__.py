from auth.hashing.strategies.abc import AbstractPasswordHashingStrategy
from .abc import AbstractPassword


class Password(AbstractPassword):
    __slots__ = ["raw", "strategy"]

    def __init__(self, password: str, strategy: AbstractPasswordHashingStrategy):
        self.raw = password
        self.strategy = strategy

    @property
    def hashed(self) -> str:
        hashed = self.strategy.hash_password(self.raw)

        return hashed

    def verify(self, hashed: str) -> bool:
        return self.strategy.verify_password(self.raw, hashed)
