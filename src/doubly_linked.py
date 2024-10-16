
# Wade McDermott


class Node:
    def __init__(self, item=None):
        self.item = item
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self):
        self.header = Node()  # Header node
        self.header.next = self.header
        self.header.prev = self.header

    def __str__(self):
        result = []
        current = self.header.next
        while current != self.header:
            result.append(str(current.item))
            current = current.next
        return "<" + ", ".join(result) + ">"

    def add_front(self, item):
        new_node = Node(item)
        first_node = self.header.next

        new_node.next = first_node
        new_node.prev = self.header
        first_node.prev = new_node
        self.header.next = new_node

    def add_back(self, item):
        new_node = Node(item)
        last_node = self.header.prev

        new_node.prev = last_node
        new_node.next = self.header
        last_node.next = new_node
        self.header.prev = new_node

    def remove_front(self):
        if self.header.next == self.header:
            raise IndexError("remove_front from an empty list")

        first_node = self.header.next
        second_node = first_node.next

        self.header.next = second_node
        second_node.prev = self.header

    def remove_back(self):
        if self.header.prev == self.header:
            raise IndexError("remove_back from an empty list")

        last_node = self.header.prev
        second_last_node = last_node.prev

        second_last_node.next = self.header
        self.header.prev = second_last_node

    def concatenate(self, other):
        if other.header.next == other.header:  # If 'other' is empty, nothing to concatenate.
            return

        first_other = other.header.next
        last_other = other.header.prev

        last_self = self.header.prev

        # Connect last node of self with first node of other
        last_self.next = first_other
        first_other.prev = last_self

        # Connect last node of other with the header of self
        last_other.next = self.header
        self.header.prev = last_other

        # Invalidate other
        other.header.next = other.header
        other.header.prev = other.header
