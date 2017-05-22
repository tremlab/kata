"""Given an array of integers arr:
Write a function flip(arr, k) that reverses the order of the first k elements 
in the array arr.  Write a function pancakeSort(arr) that sorts and 
returns the input array. You are allowed to use only the function flip 
you wrote in the first step in order to make changes in the array.
"""
import math

def flip(lst, k):
    """reverses the order of the first k elements in the array arr.
    """
    x = int(math.floor(k/2))

    for i in range(x):
        elem = lst[i]
        replace = lst[(k-i)-1] #off by one???
        lst[i] = replace
        lst[(k-i)-1] = elem

    return None


# def pancake_sort(lst):
#     end_index = len(lst)

#     for i in range(end_index,0,-1):
#         print lst[:i], "crop"
#         k = find_max_index(lst[:i])
#         print k, "index max"
#         # stop if its in the right okace
#         print k, end_index
#         if k == end_index:
#             pass
#         elif k == 0:
#             flip(lst, i)
#         else:
#             flip(lst, (k))
#             flip(lst, (i))

#     return None

def find_max_index(lst):
    """finds the INDEX of the integer of greatest value in a list.
    """
    max_int = 0
    index_max = 0

    for i in range(len(lst) - 1):
        if lst[i] >= max_int:
            max_int = lst[i]
            index_max = i
            print lst[i], max_int, index_max

    return index_max


if __name__ == '__main__':

    lst = [1,5,4,0,9,9]
    
    # pancake_sort(lst)
    flip(lst, 4)

    print lst
