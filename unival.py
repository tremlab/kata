"""code challenge - is this tree a 'unival' tree, meaning every node 
has the same data value."""


class Node(object):

    def __init__(self, value):

        self.data = value
        self.children = []


class Tree(object):

    def __init__(self, head):

        self.head = head

    def is_unival(self):

        to_evaluate = [self.head]
        value = self.head.data

        while to_evaluate:
            next = to_evaluate.pop()

            if next.data == value:
                to_evaluate.extend(next.children)
            else:
                return False

        return True

    def count_univals(self):
        """counts every unival tree within the whole tree. 
            Every leaf is its own unival tree.
        """
        def evaluate_node(node):
            if node.children == []:
                return (node.data, 1)

            count = 0
            value = node.data

            for n in node.children:
                response = evaluate_node(n)
                count += response[1]
                if response[0] != value:
                    value = None

            if value:
                count += 1

            return (value, count)

        response = evaluate_node(self.head)
        return response[1]

if __name__ == '__main__':
    """test scenario"""

    a = Node("A")
    b = Node("A")
    c = Node("A")
    d = Node("A")
    e = Node("B")
    f = Node("A")
    g = Node("A")
    h = Node("A")

    t = Tree(a)

    a.children = [b, c]
    b.children = [d, e]
    c.children = [f]
    f.children = [g, h]

    print t.is_unival()
    print t.count_univals()

