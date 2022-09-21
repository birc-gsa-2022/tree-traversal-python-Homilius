"""A module for breadth-first traversal of trees."""

import collections
from typing import Iterable
from tree import T
        
####################################
# Functions:

def count_nodes(tree):
    ''' Function for counting nodes in a tree
    
    Example:
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    count_nodes(tree)
    >5
    
    '''

    if tree == None:
        return 0
    else:
        return 1 + count_nodes(tree.left) + count_nodes(tree.right)  


def bf_order(tree):
    """Breadth-first traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(bf_order(tree))
    [2, 1, 4, 3, 5]
    """
    nodes = []
    def visit(tree):
        if tree == None:
            return 0
        if tree != None:
            if tree.val not in nodes:
                nodes.append(tree.val)
        for tree in [tree.left, tree.right]:
            if tree != None:
                nodes.append(tree.val)
            visit(tree)  
    visit(tree)
    return nodes

####################################





