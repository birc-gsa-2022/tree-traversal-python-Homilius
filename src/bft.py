"""A module for breadth-first traversal of trees."""

####################################
# Classes:

from tree import T
        
####################################
# Functions:

def count_nodes(tree):
    ''' Function for counting nodes in a tree
    
    Example:
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    count_nodes(tree)
    5
    
    '''
    if tree == None:
        return 0
    else:
        return 1 + count_nodes(tree.left) + count_nodes(tree.right)  


def visit(tree, node):
    ''' Visits specified node
    
    Example:
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    visit(tree, 4)
    T(val=4, left=T(val=3, left=None, right=None), right=T(val=5, left=None, right=None))
    
    '''
    if tree == None:
        return None
    if tree.val == node:
        return tree
    for subtree in [tree.left,tree.right]:
        if subtree != None:
            if subtree.val == node:
                return subtree
            visit(subtree, node)


def bf_order(tree):
    """Breadth-first traversal of a tree.
    
    Example:
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    bf_order(tree)
    [2, 1, 4, 3, 5]
    
    """
    nodes = []
    if tree == None:
        return []
    if tree != None:
        nodes.append(tree.val)
    sub = [tree.left, tree.right]
    for subtree in sub:
        if subtree != None and subtree.val not in nodes:
            nodes.append(subtree.val)
            sub.append(subtree.left)
            sub.append(subtree.right)
        bf_order(subtree)
    return nodes

####################################


