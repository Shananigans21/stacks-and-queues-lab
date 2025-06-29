def is_valid_parentheses(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in pairs.values():  # opening bracket
            stack.append(char)
        elif char in pairs:  # closing bracket
            if not stack or stack.pop() != pairs[char]:
                return False
        # ignore other characters if any (or assume only brackets)

    return not stack  # True if stack empty (all matched)
