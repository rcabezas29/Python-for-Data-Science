def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """
    Receives two lists, one with weights and other with heights. They belong
    respectively to the same person for every position. It apply with that
    information the formula to return a the BMI for every person.
    """
    try:
        assert len(height) == len(weight), "Lists must be the same size"
        assert len(height) > 0, "Not a valid list size"
        for i, j in height, weight:
            assert i > 0, "Invalid height in list"
            assert j > 0, "Invalid weight in list"
        return [b / a**2 for a, b in zip(height, weight)]
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Returns an array with the bool result of checking if the values of
    another list are bigger than a limit.
    """
    try:
        assert len(bmi) > 0, "Empty list"
        return [x > limit for x in bmi]
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return []
