class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # self.left and/or self.right need to be valid nodes
        # for us to call insert on them
        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            else:
                # we have found a valid parking spot
                self.left = BinarySearchTreeNode(value)
        # otherwise, value >= self.value:
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass


'''
    # recursive insert implementation
    def insert(self, value):
        # base case: we found a parking spot
        # We are in an empty spot in the tree
        if self is None:
            self = BinarySearchTreeNode(value)
        # if we are not at the base case, move towards it
        else:
            # self is a node with a value
            # compare the value to the value at this node
            if value < self.value:
                # move to the left
                self.left.insert(value)
            # otherwise, value >= self.value
            else:
                self.right.insert(value)
'''