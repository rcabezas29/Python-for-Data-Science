import sys


def morse_equivalence(c: str) -> str:
    """
    Returns the equivalemce of the char passed as argument with its equivalence
    in morse code.
    It throws an AssertionError if 'c' has no equivalence in morse.
    """
    morse = {
        'a': '.- ',
        'b': '-... ',
        'c': '-.-. ',
        'd': '-.. ',
        'e': '. ',
        'f': '..-. ',
        'g': '--. ',
        'h': '.... ',
        'i': '.. ',
        'j': '.--- ',
        'k': '-.- ',
        'l': '.-.. ',
        'm': '-- ',
        'n': '-. ',
        'o': '--- ',
        'p': '.--. ',
        'q': '--.- ',
        'r': '.-. ',
        's': '... ',
        't': '- ',
        'u': '..- ',
        'v': '...- ',
        'w': '.-- ',
        'x': '-..- ',
        'y': '-.-- ',
        'z': '--.. ',
        '1': '.---- ',
        '2': '..--- ',
        '3': '...-- ',
        '4': '....- ',
        '5': '..... ',
        '6': '-.... ',
        '7': '--... ',
        '8': '---.. ',
        '9': '----. ',
        '0': '----- ',
        ',': '--..-- ',
        '.': '.-.-.- ',
        '?': '..--.. ',
        '/': '-..-. ',
        '-': '-....- ',
        '(': '-.--. ',
        ')': '-.--.- ',
        ' ':  '/ '
    }
    assert c in morse, "the arguments are bad"
    return morse[c]


def main():
    """
    Takes a string as an argument and encodes it into Morse Code.

    • The program supports space and alphanumeric characters.

    • An alphanumeric character is represented by dots . and dashes -.

    • Complete morse characters are separated by a single space.

    • A space character is represented by a slash /
    """
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        morse = ""
        for i in sys.argv[1].lower():
            morse += morse_equivalence(i)
        print(morse)
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
