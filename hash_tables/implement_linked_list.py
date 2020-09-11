class Node:

    def __init__(self, data):
        self.value = data
        self.next_node = None

    def __repr__(self):
        return self.value    

class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next_node = Node(data=elem)
                node = node.next_node

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
            node = node.next_node    

    def insert(self, newNode):
        """
        add the new element to the head.
        """
        newNode.next_node = self.head
        self.head = newNode
    
    def add_last(self, newNode):
        if not self.head:
            self.head = newNode
            return
        for cur_node in self:
            pass
        cur_node.next_node = newNode

    def add_after(self, target_node_data, newNode):
        if not self.head:
            raise Exception("The list is empty")
        for cur_node in self:
            if cur_node.value == target_node_data:
                newNode.next_node = cur_node.next_node
                cur_node.next_node = newNode
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("The list is empty")
        
        # if wee need to remove head node
        if self.head.value == target_node_data:
            self.head = self.head.next_node
            return

        previous_node = self.head
        for cur_node in self:
            if cur_node.value == target_node_data:
                previous_node.next_node = cur_node.next_node
                return
            previous_node = cur_node 

        raise Exception("Node with data '%s' not found" % target_node_data)    



if __name__=="__main__":
    llist = LinkedList(["a", "b", "c", "d"])
    llist.insert(Node("a1"))
    llist.add_last(Node("f"))
    print(llist)
    llist.remove_node('r')
    print(llist)