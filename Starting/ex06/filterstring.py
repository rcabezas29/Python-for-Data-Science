import sys
from ft_filter import ft_filter


def can_convert_to_int(s: str) -> bool:
    """
    This functions checks if a str can be converted into an 'int'
    in order to throw an Assertion Exception
    """
    try:
        int(s)
        return True
    except ValueError:
        return False


def length_is_greater_than(s: str, n: int = 5) -> bool:
    """
    Checks if a str is at least n length.
    """
    return len(s) >= n


def aux_func(x):
    """
    Aux function in order that reduces function to one parameter
    """
    return length_is_greater_than(x, int(sys.argv[2]))


def main():
    """
    It should output a list of words from S that have a length greater than N.

    • Words are separated from each other by space characters.

    • Strings do not contain any special characters. (Punctuation or invisible)

    • The program must contain at least one list comprehension expression and
    one lambda.

    • If the number of argument is different from 2, or if the type of any
    argument is wrong, the program prints an AssertionError.

    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert can_convert_to_int(sys.argv[2]), "the arguments are bad"
        words = sys.argv[1].split(' ')
        a = ft_filter(aux_func, words)
        print(a)
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
