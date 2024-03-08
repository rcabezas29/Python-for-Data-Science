from S1E9 import Character


class Baratheon(Character):
    """
    Representing the Baratheon family
    """
    def __init__(self, first_name=None, is_alive=True):
        """
        Baratheon constructor that sets their house words and family name
        """
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Baratheon"
        self.house_words = "Ours is the Fury"
        self.eyes = "Brown"
        self.hairs = "dark"

    def print_house_words(self):
        """
        Prints Baratheons house words
        """
        print(self.house_words)

    def die(self):
        """
        Sets alive attribute to False.
        """
        self.is_alive = False

    def __repr__(self) -> str:
        """
        Represent function
        """
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __str__(self) -> str:
        """
        String function
        """
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"


class Lannister(Character):
    """
    Representing the Lannister family
    """
    def __init__(self, first_name=None, is_alive=True):
        """
        Lannister constructor that sets their house words and family name
        """
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar"
        self.eyes = "Bluse"
        self.hairs = "light"

    def print_house_words(self):
        """
        Prints Lannisters house words
        """
        print(self.house_words)

    def die(self):
        """
        Sets alive attribute to False.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, name: str, alive: bool):
        """
        Creates an instance of a Lannister
        """
        return cls(name, alive)

    def __repr__(self) -> str:
        """
        Represent function
        """
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __str__(self) -> str:
        """
        String function
        """
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"
