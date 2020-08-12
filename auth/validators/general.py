from .abc import AbstractValidator


class LengthValidator(AbstractValidator):
    def __init__(self, min_length: int, max_length: int):
        self.min_length = min_length
        self.max_length = max_length

    def valid(self, text: str) -> bool:
        text_length = len(text)

        return (
            (text_length > self.min_length) and
            (text_length < self.max_length)
        )
