"""sort for big numbers.  (too big for normal int use)
"""


# need to optimize!!! works fine, but meant for 
# gigantic strings of gigantic numbers.

def big_sort(unsorted):

    strings = {}
    for i in unsorted:
        st = str(i)
        l = len(st)
        # convert all to strings
        # put into buckets of similar lengths
        if l in strings:
            strings[l].append(st)
        else:
            strings[l] = [st]
    # sort lengths (of each bucket)
    lengths = strings.keys()
    lengths.sort()
    # sort items in each bucket
    for l in lengths:
        sts = strings[l]
        ints = []
        for s in sts:
            ints.append(int(s))
        ints.sort()
        
        for n in ints:
            print n


nums = [6,
31415926535897932384626433832795,
1,
3,
10,
3,
5]

big_sort(nums)

