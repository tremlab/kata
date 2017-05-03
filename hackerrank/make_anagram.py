"""Hackerrank challenge - count how many letters must be deleted to make 
to make 2 strings anagrmas of each other.
"""


def number_needed(a, b):
    
    a_list = list(a)
    a_list.sort()
    b_list = list(b)
    b_list.sort()
    
    count = 0
    
    while a_list and b_list:
                
        if a_list[-1] != b_list[-1]:
            count += 1
            
            if a_list[-1] > b_list[-1]:
                a_list.pop()
            else:
                b_list.pop()
        
        else:
            a_list.pop()
            b_list.pop()

    if a_list:
        count += len(a_list)

    if b_list:
        count += len(b_list)
       
    return count

a = "elephant"
b = "elaphantiiiiii"

print number_needed(a, b)