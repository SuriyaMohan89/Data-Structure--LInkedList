class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node object. Data: %s; Next: %s>" % (
                                        self.data,
                                        self.next.data if self.next else None,
                                        )


class LinkedList(object):

    def __init__(self):
        self.h1 = None
        self.h2 = None
        self.t1 = None
        # self.t2 = None

    def find_converging_node(self):
        """This works only if two diverged LinkedList is of same length"""

        if self.h1 is None or self.h2 is None:
            return None

        current_node_l1 = self.h1
        current_node_l2 = self.h2

        while current_node_l2 != None or current_node_l1 != None:
            if current_node_l1.next == current_node_l2.next:
                return current_node_l2.next
            current_node_l1 = current_node_l1.next
            current_node_l2 = current_node_l2.next

        return "No converging Nodes"

        """ This works for all condtions but not an optimized solution"""

        if self.h1 is None or self.h2 is None:
            return None

        current_node_l1 = self.h1

        while current_node_l1 is not None:
            current_node_l2 = self.h2
            while current_node_l2 is not None:
                if current_node_l1.next == current_node_l2.next :
                    return current_node_l2.next
                current_node_l2 = current_node_l2.next
            current_node_l1 = current_node_l1.next

        return "No converging nodes"

        if self.h1 is None or self.h2 is None:
            return None

        current_node_l1 = self.h1

        while current_node_l1 is not None:
            current_node_l2 = self.h2
            while current_node_l2 is not None:
                if current_node_l1 == current_node_l2:
                    return current_node_l2
                current_node_l2 = current_node_l2.next
            current_node_l1 = current_node_l1.next

        return "No converging nodes"


  