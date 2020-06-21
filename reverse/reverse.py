class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # If list is not empty
        if self.head:
            # If we are at the end of the list
            if node.get_next() == None:
                # set new head to old last item
                self.head = node
                # end func
                return
            # call recursively, passing in next node
            self.reverse_list(node.get_next(), node)
            temp = node.get_next()
            temp.set_next(node)
            node.set_next(None)
        else: 
            # If list is empty, return False
            return False

