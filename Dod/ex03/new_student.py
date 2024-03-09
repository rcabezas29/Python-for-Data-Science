import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

def create_login(name: str, surname: str) -> str:
    """
    Creates a login based on name and surname
    """
    return name[0] + surname[:7]


@dataclass
class Student:
    """
    Class Student
    """
    name: str
    surname: str
    active: bool = True
    id: str = field(default_factory=generate_id)
    login: str = field(default_factory="")
