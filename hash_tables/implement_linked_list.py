class Node:
    def __init__(self, data):
        self.value = data
        self.next_node = None

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None      