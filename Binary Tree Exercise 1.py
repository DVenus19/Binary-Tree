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