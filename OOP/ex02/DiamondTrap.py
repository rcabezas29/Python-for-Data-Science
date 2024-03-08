from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Representing the King
    """
    def __init__(self, name, alive=True):
        super().__init__(name, alive)

    def set_eyes(self, eyes):
        """
        Setter of eye color
        """
        self.eyes = eyes

    def get_eyes(self):
        """
        Getter eyes
        """
        return self.eyes

    def set_hairs(self, hair):
        """
        Setter of hair color
        """
        self.hairs = hair

    def get_hairs(self):
        """
        Getter hairs
        """
        return self.hairs
