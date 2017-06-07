def is_matched(expression):
    dict_b = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    stack = []

    for char in expression:
        if char in dict_b.values():
            stack.append(char)
        elif char in dict_b.keys():
            if stack:
                most_recent = stack.pop()
                if most_recent != dict_b[char]:
                    return False
            else:
                return False

    return stack == []


print is_matched("{[()]}")
print is_matched("{[(])}")
print is_matched("{{[[(())]]}})()()()()()()()()()(){}{}{}{}{}{}")
