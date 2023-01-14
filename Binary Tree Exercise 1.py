print("**********DSA - Binary Tree Exercise 1**********")
print("**********Programmed by : Donasco,Venus M.")
print("********** BSCOE 2-2 **********")


#Adding the methods to the BinarySearchTreeNode class created in main video tutorial
#Using my fullname as the content of the binary tree

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    #finds minimum element in entire binary tree
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    #finds maximum element in entire binary tree
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    #calculates the sum of all elements
    def calculate_sum(self):
        elements = self.in_order_traversal()
        Total_Value = 0
        for i in range(len(elements)):
            Total_Value += elements[i]

        return Total_Value

    #performs post order traversal of a binary tree
    def post_order_traversal(self):
        elements = []

        #First,visiting the left side
        if self.left:
            elements += self.left.post_order_traversal()

        #Second,visiting the right side
        if self.right:
            elements += self.right.post_order_traversal()

        # Visit the node last.
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):  # performs pre order traversal of a binary tree
        elements = []
