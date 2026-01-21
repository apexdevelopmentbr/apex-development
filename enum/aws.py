from enum import Enum


class AWS(str, Enum):
    def __str__(self):
        return self.value

    SECRETMANAGER = 'secretsmanager'