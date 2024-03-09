def square(x: int | float) -> int | float:
    """
    Power of 2
    """
    return x**2


def pow(x: int | float) -> int | float:
    """
    Power of itself
    """
    return x**x


def outer(x: int | float, function) -> object:
    """Outer function to store the last result"""
    count = 0
    res = x

    def inner() -> float:
        """
        Inner function that is executed
        """
        nonlocal count
        nonlocal res
        res = function(res)
        return res

    return inner
