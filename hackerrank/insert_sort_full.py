def insertionSort(ar):
    
    for i in range(2, len(ar)+1):
        cropped_list = ar[0:i]
        this_sort = insert_item(cropped_list)
        ar = this_sort + ar[i:]
        for n in ar:
            print n,
        print "\r"
    

def insert_item(ar):
    item = ar[-1]

    for i in range(len(ar)-2, -1, -1):
        if ar[i] < item:
            ar[i+1] = item
            item = None
            return ar
        else:
            ar[i+1] = ar[i]

    if item:
        ar[0] = item
    
    return ar


nums = [1, 4, 3, 5, 6, 2]
insertionSort(nums)
