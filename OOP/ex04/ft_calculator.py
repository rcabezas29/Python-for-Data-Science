class calculator:
    """
    It is able to do calculations (dot product, addition, subtraction)
    of 2 vectors without being instantiated.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Applies and prints a dot product over 2 vectors
        """
        dp = 0
        for i in range(len(V1)):
            dp += (V1[i] * V2[i])
        print(f"Dot product is: {dp}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Applies and prints an addition of 2 vectors
        """
        print(f"Add Vector is: {[x + y for x, y in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Applies and prints a substraction of 2 vectors
        """
        print(f"Sous Vector is: {[x - y for x, y in zip(V1, V2)]}")
