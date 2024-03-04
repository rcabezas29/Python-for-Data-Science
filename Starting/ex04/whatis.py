import sys


def can_convert_to_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    assert can_convert_to_int(sys.argv[1]), "argument is no t an integer"

    x = int(sys.argv[1])

    if x % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as msg:
    print(f"Assertion error: {msg}")
except IndexError:
    ''''''
