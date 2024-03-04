import sys
import string


def manage_input():
    """
    Manages input to count return carriage as a space and end with ctrl+d
    """
    print("What is the text to count?")
    entered_text = ""
    try:
        while True:
            char = sys.stdin.read(1)
            if not char:
                break
            if char == '\n':
                char = ' '
            entered_text += char
    except EOFError:
        pass
    return entered_text


def main():
    """
    Takes a single string argument and displays the sums of its
    upper-case characters, lower-case characters, punctuation
    characters, digits and spaces.
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    if len(sys.argv) < 2:
        text = manage_input()
    else:
        text = sys.argv[1]
    u, l, p, s, d = 0, 0, 0, 0, 0
    for c in text:
        if c.islower():
            l += 1
        elif c.isupper():
            u += 1
        elif c in string.punctuation:
            p += 1
        elif c.isspace():
            s += 1
        elif c.isdigit():
            d += 1
    print(f"The text contains {len(text)} characters:")
    print(f'{u} upper letters')
    print(f'{l} lower letters')
    print(f'{p} punctuation marks')
    print(f'{s} space(s)')
    print(f'{d} digits')


if __name__ == "__main__":
    main()
