import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # self.left and/or self.right need to be valid nodes
        # for us to call insert on them
        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            else:
                # we have found a valid parking spot
                self.left = BinarySearchTree(value)
        # otherwise, value >= self.value:
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
        elif target > self.value and self.right is not None:
            return self.right.contains(target)
        else:
            return False    

    # Return the maximum value found in the tree
    def get_max(self):
        # base case
        # if empty tree, return none
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
        # recursive case
        # if there is no right value
            # return the root node value
        # otherwise
            # return get max of the right hand child

    # Call the function `cb` on the value of each node
    # Apply the callback function to every single node of our tree
    # at least, O(n), could be worse depending on the callback
    def for_each(self, cb):
        # apply the callback
        cb(self.value)
        # base case: the node has no children

        # call the cb on the children of this node
        # let's check this node has children
        if self.left:
           self.left.for_each(cb)
        if self.right:
           self.right.for_each(cb)



    def depth_first_iterative_for_each(self, cb):
        stack = []
        # add the root of the tree to the stack
        stack.append(self)

        # loop so long as the stack still has elements
        while len(stack) > 0:
            current_node = stack.pop()
            # check if the right child exists
            if current_node.right:
                stack.append(current_node.right)
            # check if the left child exists
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)


    def breadth_first_iterative_for_each(self, cb):
        # depth first: stack
        # breadth first: queue
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.pop.left()
            if current_node.left:
                q.append(current_node.value)
            if current_node.right:
                q.append(current_node.value)
'''
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

'''