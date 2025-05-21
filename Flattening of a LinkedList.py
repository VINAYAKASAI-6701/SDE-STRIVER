class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

class Solution:
    def merge(self, a, b):
        dummy = Node(0)
        temp = dummy

        while a is not None and b is not None:
            if a.data < b.data:
                temp.bottom = a
                a = a.bottom
            else:
                temp.bottom = b
                b = b.bottom
            temp = temp.bottom

        if a is not None:
            temp.bottom = a
        else:
            temp.bottom = b

        return dummy.bottom

    def flatten(self, root):
        if root is None or root.next is None:
            return root

        # Recurse on right
        root.next = self.flatten(root.next)

        # Merge current list with next list
        root = self.merge(root, root.next)

        # To avoid confusion and ensure `.next` is not used further
        root.next = None

        return root
