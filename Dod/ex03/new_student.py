import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


def create_login(name: str, surname: str) -> str:
    """
    Creates a login based on name and surname
    """
    return (name[0] + surname[:7]).lower()


@dataclass
class Student:
    """
    Class Student
    """
    name: str
    surname: str
    active: bool = field(default=True)
    id: str = field(default_factory=generate_id, init=False)
    login: str = field(init=False)

    def __post_init__(self):
        """
        Creates the login after the instantiation of the class
        as name and surname are not generated previously
        """
        self.login = create_login(self.name, self.surname)
