def rev_words_efficient(arr):
    arr.reverse()

    start = 0

    for i in range(len(arr)):
        if arr[i] == "  ":
            stop = i - 1
            mirror(start, stop, arr)
            start = i + 1

    mirror(start, len(arr) - 1, arr)

    return arr


def mirror(start, stop, arr):
    while start < stop:

        arr[start], arr[stop] = arr[stop], arr[start]
        start += 1
        stop -= 1





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


print reverseWords(['c', 'a', 't', '  ', 'f', 'a', 't'])
print rev_words_efficient(['c', 'a', 't', '  ', 'f', 'a', 't', 't', 'y'])
