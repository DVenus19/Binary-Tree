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
            if self_left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #adding data in the right subtree
            if self_right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

def in_order_travesal(self):
    elements = []

    #visit left tree
    if self.left:
        elements += self.left.in_order_traversal()

    #visit base node
    elements.append(self.data)

    #visit right tree
    if self.right:
        elements += self.right.in_order_traversal()

    return elements

if __name__ == '__main__':



