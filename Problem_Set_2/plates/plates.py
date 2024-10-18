def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if starts_with_two_letters(s) and max_6_letters(s) and plate_is_alnum(s) and rule3(s):
        return True
    return False

# Rule 1
# All vanity plates must start with at least two letters


def starts_with_two_letters(s):
    if s[0:1].isalpha():
        return True
    return False
# Rule 2
# … vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.


def max_6_letters(s):
    if 2 <= len(s) <= 6:
        return True
    return False
# Rule 3
# Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.


def rule3(s):
    # Max 6 would be checked by other rule
    # Cut string from 2 to end
    s = s[2:]
    if '0' in s:
        if s.index('0') == 0:
            return False
        elif s.index('0') == 1 and s[0].isnumeric() and s[1:].isnumeric():
            return True
        elif s.index('0') == 2 and s[0:1].isalnum() and s[2:].isnumeric():
            return True
        elif s.index('0') == 3 and s[0:2].isalnum():
            return True
        return False
    else:
        if s[0].isalpha() and s[1:].isalpha():
            return True
        elif s[0].isnumeric() and s[1:].isnumeric():
            return True
        elif s[0:1].isalpha() and s[1:].isnumeric():
            return True
        elif s[0:2].isalpha() and s[2:].isnumeric():
            return True
        return False

# Rule 4
# No periods, spaces, or punctuation marks are allowed.


def plate_is_alnum(s):
    if s.isalnum():
        return True
    return False

main()
