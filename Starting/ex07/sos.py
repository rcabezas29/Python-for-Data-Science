import sys


NESTED_MORSE = {
    'A': '.- ',
    'a': '.- ',
    'B': '-... ',
    'b': '-... ',
    'C': '-.-. ',
    'c': '-.-. ',
    'D': '-.. ',
    'd': '-.. ',
    'E': '. ',
    'e': '. ',
    'F': '..-. ',
    'f': '..-. ',
    'G': '--. ',
    'g': '--. ',
    'H': '.... ',
    'h': '.... ',
    'I': '.. ',
    'i': '.. ',
    'J': '.--- ',
    'j': '.--- ',
    'K': '-.- ',
    'k': '-.- ',
    'L': '.-.. ',
    'l': '.-.. ',
    'M': '-- ',
    'm': '-- ',
    'N': '-. ',
    'n': '-. ',
    'O': '--- ',
    'o': '--- ',
    'P': '.--. ',
    'p': '.--. ',
    'Q': '--.- ',
    'q': '--.- ',
    'R': '.-. ',
    'r': '.-. ',
    'S': '... ',
    's': '... ',
    'T': '- ',
    't': '- ',
    'U': '..- ',
    'u': '..- ',
    'V': '...- ',
    'v': '...- ',
    'W': '.-- ',
    'w': '.-- ',
    'X': '-..- ',
    'x': '-..- ',
    'Y': '-.-- ',
    'y': '-.-- ',
    'Z': '--.. ',
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
        for c in sys.argv[1]:
            assert c in NESTED_MORSE, "the arguments are bad"
            morse += NESTED_MORSE[c]
        print(morse)
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
