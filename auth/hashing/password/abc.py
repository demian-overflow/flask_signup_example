from abc import ABC


class AbstractPassword(ABC):
    @property
    def hashed(self) -> str:
        raise NotImplementedError

    def verify(self, hashed: str) -> bool:
        raise NotImplementedError
