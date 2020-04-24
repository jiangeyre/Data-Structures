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
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
           self.left.for_each(cb)
        if self.right is not None:
           self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
           self.left.in_order_print(self.left)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            node = q.dequeue()
            print(node.value)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
          return
        s = Stack()
        s.push(node)
        while s.size > 0:
            node = s.pop()
            print(node.value)
            if node.left is not None:
                s.push(node.left)
            if node.right is not None:
                s.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

