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


####### I considered two linked list with heads h1 and h2. There many ways to do. I chose to have a Linked List class 
####### But also possible to just do with Node class

    def __init__(self):
        self.h1 = None
        self.h2 = None

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


    def find_converging_node(self):        
        """ This works even if not of same length but throws error on a condition where there is no next"""

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

    def find_converging_node(self):
        """ This works for all conditions but can be optimized"""

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


  