print("**********DSA - Binary Tree Exercise 2**********")
print("**********Programmed by : Donasco,Venus M.")
print("********** BSCOE 2-2 **********")

#Modify delete method in class BinarySearchTreeNode class to use min element from left subtree and using max value from left subtree

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

