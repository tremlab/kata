def reverseWords(arr):
    words = []
    word = []

    for char in arr:

        if char == "  ":
            words.append(word)
            word = []
        else:
            word.append(char)

    words.append(word)

    words.reverse()

    reversed_list = []

    for word in words:
        word.append("  ")
        reversed_list.extend(word)

    reversed_list.pop()

    return reversed_list


print reverseWords([ 'c', 'a', 't', '  ', 'f', 'a', 't'])
