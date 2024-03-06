def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start
    and end arguments.
    """
    try:
        row_lengths = [len(row) for row in family if isinstance(row, list)]
        assert row_lengths, "There are non-list elements."
        assert len(set(row_lengths)) == 1, "lists are not the same size"
        print(f"My shape is {(len(family), len(family[0]))}")
        truncated = family[start:end]
        print(f"My new shape is {(len(truncated), len(truncated[0]))}")
        return truncated
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return []
