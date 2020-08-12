from .password import Password
from .strategies import BCryptPasswordHashingStrategy

from settings import AUTH_HASHING_SALT_SIZE


hashing_strategy = BCryptPasswordHashingStrategy(AUTH_HASHING_SALT_SIZE)
