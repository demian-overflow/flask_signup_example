from abc import ABC


class AbstractValidator(ABC):
    def valid(self, text: str) -> bool:
        raise NotImplementedError
