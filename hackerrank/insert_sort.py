def insertionSort(ar):
    """takes in a list of sorted items, excpet the LAST item is a 
    random value to be correctly inserted.
    hacerrank output required that each step be printed.
    """

    item = ar[-1]

    for i in range(len(ar)-2, -1, -1):
        if ar[i] < item:
            ar[i+1] = item
            item = None
            for n in ar:
                print n,
            print "\r"
            return
        else:
            ar[i+1] = ar[i]
            for n in ar:
                print n,
            print "\r"

    if item:
        ar[0] = item
        for n in ar:
            print n,
        print "\r"

nums = [2, 4, 6, 8, 3]

insertionSort(nums)
