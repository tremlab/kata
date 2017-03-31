def ransom_note(magazine, ransom):
    """chekc if all the EXACT words needed for the note are present 
    in the magazine text. Returns True or False.
    """
    
    avail_words = {}
    
    for w in magazine:
        if w in avail_words:
            avail_words[w] += 1
        else:
            avail_words[w] = 1

    print avail_words
    
    for w in ransom:
        if w in avail_words:
            if avail_words[w] > 0:
                print w, avail_words[w]

                avail_words[w] -= 1
            else:
                return False
        else:
            return False
    
    return True



magazine = "hello you frank".strip().split(' ')

ransom = "hello you you you you".strip().split(' ')

print ransom_note(magazine, ransom)


"""Congrats, you solved this challenge!
 Test Case #0
 Test Case #1
 Test Case #2
 Test Case #3
 Test Case #4
 Test Case #5
 Test Case #6
 Test Case #7
 Test Case #8
 Test Case #9
 Test Case #10
 Test Case #11
 Test Case #12
 Test Case #13
 Test Case #14
 Test Case #15
 Test Case #16
 Test Case #17
 Test Case #18
 Test Case #19
"""