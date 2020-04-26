
class Node:
    """ Node class Constructor
        input: val - value of the node
    """
    def __init__(self, val):
        self.leftChild = None
        self.rightChild = None
        self.value = val

    def insert(self, data):
        # check if node already has this value
        # ti avoid duplicates
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True


class BinarySearchTree:
    """ Tree class Constructor
        root node is null
    """
    def __init__(self):
        """ Constructor
        """
        self.root = None

    def insert(self, data):
        """
        Insert new node into the BST
        """
        if self.root:
            return self.root.insert(data)
        else:
            # if there is no nodes in the tree then create a new root node
            self.root = Node(data)
            return True
