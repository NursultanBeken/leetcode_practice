class Node:

    def __init__(self, data):
        self.value = data
        self.next_node = None

    def __repr__(self):
        return self.value    

class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next_node
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """
        traverse a Linked list
        """
        node = self.head
        while node is not None:
            yield node
            node.next_node = node    

    def insert(self, newValue):
        """
        add the new element to the head.
        """
        newNode = Node(newValue)
        newNode.next_node = self.head
        self.head = newNode
    
    def append_to_end(self, newValue):
        newNode = Node(newValue)
        if not self.head:
            self.head = newNode
            return
        for cur_node in self:
            pass
        cur_node.next_node = newNode    