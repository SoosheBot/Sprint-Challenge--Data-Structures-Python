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
    #     #To-dos:
    #     # Initialize pointers, previous and node as None, current_node as self.head -- there is nothing in the previous or future nodes, which is why they are None, which is why we are currently in self.head
    #     # Now to iterate through linked list 
    #     ## You need to set up the next node coming up as the current-next node and what used to be the old current node becomes the previous node
    #     ## THEN the previous node becomes the current_node and the current_node becomes the next node
    #     ## The head moves to the previous node, since it's gotta travel backwards with the reversal.
        prev = None
        node = None
        current_node = self.head

        while current_node is not None:
            next = current_node.next_node
            current_node.next_node = prev
            prev = current_node
            current_node = next
            self.head = prev
        return prev

           