"""A module for depth-first (in-order) traversal of trees."""

################################################################
# Classes:

from tree import T

################################################################
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


def in_order(tree):
    '''In-order traversal of a tree.
    
    Example:
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    in_order(tree)
    [1, 2, 3, 4, 5]

    '''
    nodes = []
    stack = [tree]
    while len(stack) > 0:
        candidate = stack.pop()
        if candidate == None:
            if len(stack) == 0:
                return nodes
            candidate = stack.pop()
            nodes.append(candidate)
        else:  # must be this order!
            stack.append(candidate.right)
            stack.append(candidate.val)
            stack.append(candidate.left)


################################################################
