def match_brackets(string):
    open_brackets = []

    for char in string:
        if char in ('(', '{', '['):
            open_brackets.append(char)
        elif char in (')', '}', ']'):
            if not open_brackets:
                return False
            elif char == open_brackets[-1]:
                open_brackets.pop()
            else:
                return False

    return not open_brackets
