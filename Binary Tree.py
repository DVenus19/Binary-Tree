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
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #adding data in the right subtree
            if self.right:
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

    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                pass
            else:
                return False
        if val > self.data:
            #val might be in right subtree



def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34,18,4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_travesal())


