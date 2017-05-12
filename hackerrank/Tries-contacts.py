class Node(object):  
    def __init__(self, value, is_end=False):
        self.data = value
        self.children = {}
        self.is_end = is_end


class ContactTry(object):
    def __init__(self):
        self.head = Node("")

    def add_name(self, name):
        n_letters = list(name)
        current = self.head

        for l in n_letters:
            if l in current.children:
                current = current.children[l]
            else:
                current.children[l] = Node(l)
                current = current.children[l]

        current.is_end = True

    def count_matches(self, start):
        count = 0
        n_letters = list(start)
        current = self.head

        for l in n_letters:
            if l in current.children:
                current = current.children[l]
            else:
                return 0

        if current.is_end:
            count += 1
        l_paths = current.children.values()

        while l_paths:
            next = l_paths.pop()
            if next.is_end:
                count += 1
            l_paths.extend(next.children.values())

        return count

contacts = ContactTry()

# hackerank syntax
############################
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
############################

    if op == "add":
        contacts.add_name(contact)
    else:
        count = contacts.count_matches(contact)
        print count
