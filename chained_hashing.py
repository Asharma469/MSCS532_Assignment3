class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

# linked list insert.
    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        current = self.head
        previous = None

        # Delete the first node matching the key and return True if removed.
        while current is not None:
            if current.key == key:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next

        return False

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.key, current.value
            current = current.next
