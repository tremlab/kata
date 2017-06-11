def partition(ar):
    """takes a list and partitions on the value of the first element.
    """

    p = ar[0]
    left = []
    equal = []
    right = []

    for n in ar:
        if n < p:
            left.append(n)
        elif n > p:
            right.append(n)
        else:
            equal.append(n)

    p_sort = left + equal + right

    for n in p_sort:
        print n,

nums = [4, 5, 3, 7, 2]
partition(nums)