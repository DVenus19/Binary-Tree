print("**********DSA - Binary Tree**********")
print("**********Programmed by : Donasco,Venus M.")
print("********** BSCOE 2-2 **********")

class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            #adding data in the left subtree
        else:
            #adding data in the right subtree

