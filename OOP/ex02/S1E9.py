from abc import ABC, abstractmethod


class Character(ABC):
    """
    Absatract class for every kind of GOT character
    """

    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """
        Character class constructor.
        Instantiates all characters from which this class is
        inheriting.
        """
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(Character):
    """
    Stark class - The winter is coming.
    Inherits from Character.
    """

    def __init__(self, first_name=None, is_alive=True):
        """
        Stark constructor that sets their house words and family name
        """
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        """
        Prints Starks house words
        """
        print(self.house_words)

    def die(self):
        """
        Sets alive attribute to False.
        """
        self.is_alive = False
