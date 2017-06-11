def insertion_sort(ar):   
    n_swaps = 0
    
    for i in range(2, len(ar)+1):
        cropped_list = ar[0:i]
        this_sort = insert_item(cropped_list)
        swapped = True
        for i in range(len(cropped_list)):
            if cropped_list[i] != this_sort[i]:
                swapped = False
                break
        if swapped:
            n_swaps += 1
        ar = this_sort + ar[i:]

    return n_swaps
    

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


nums = [2, 1, 3, 1, 2]
x = insertion_sort(nums)
print x
print x == 4