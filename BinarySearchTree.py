# File containing most important functions for the basic Binary Searcth Tree Datastructure


class node:
    def __init__(self, value, left_child=None, right_child=None, parent=None):
        self.value = value
        self.left_child = left_child
        self.right_child = left_child
        self.parent = parent
        self.data = {}
        
def insert(root, node):
    '''
    Function for inserting a node into a tree
    '''
    y = None
    x = root
    
    while x !=None:
        y = x
        if node.value < x.value:
            x = x.left_child
        else:
            x = x.right_child
    
    node.parent = y
    if y is None:
        root = node
    elif node.value < y.value:
        y.left_child = node
    else:
        y.right_child = node

def minimum_node(node):
    '''
    Finding left-most (minimum value) node in subtree from node x
    '''
    while node.left_child is not None:
        node = node.left_child
    return node
    
def maximum_node(node):
    '''
    Finding right-most (maximum value) node in subtree from node x
    '''
    while node.right_child is not None:
        node = node.right_child
    return node
   
def search(root, value):
    '''
    Looks for a node with value given in function argument
    '''
    if root is None or root.value == value:
        return root

    if value > root.value:
        return search(root.right_child, value)

    return search(root.left_child, value)
    
def successor(node):
    '''
    Finds the successor for a specific node
    '''
    if node.right_child is not None:
        return minimum_node(node.right_child)
    y = node.parent
    while y is not None and node == y.right_child:
        node = y
        y = y.parent
    return y
    
def predecessor(node):
    '''
    Finds the predecessor for a specific node
    '''
    if node.left_child is not None:
        return maximum_node(node.left_child)
    y = node.parent
    while y is not None and node == y.left_child:
        node = y
        y = y.parent
    return y

def transplant(root, node1, node2):
    '''
    Helper function for deletion
    '''
    if node1.parent is None:
        root = node2
    elif node1 == node1.parent.left_child:
        node1.parent.left_child = node2
    else:
        node1.parent.right_child = node2
    
    if node2 is not None:
        node2.parent = node1.parent
        
def deletion(root, node):
    '''
    Deletes a specfic node in a BST
    '''
    if node.left_child is None:
        transplant(root, node, node.right_child)
    elif node.right_child is None:
        transplant(root, node, node.left_child)
    else:
        y = minimum_node(node.right_child)
        if y.parent != node:
            transplant(root, y, y.right_child)
            y.right_child = node.right_child
            y.right_child.parent = y
        
        transplant(root, node, y)
        y.left_child = node.left_child
        y.left_child.parent = y
