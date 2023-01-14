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

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def build_tree(elements):
    print("Building tree with these following elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':

    numbers_tree = build_tree([5, 41, 3, 20, 19, 67, 10, 15, 78, 18, 33, 65, 89])
    print("\nIn order traversal: ", numbers_tree.in_order_traversal())
    numbers_tree.delete(3)
    print("After deleting number 3: ", numbers_tree.in_order_traversal())
    numbers_tree.delete(67)
    print("After deleting number 67: ", numbers_tree.in_order_traversal())
    numbers_tree.delete(10)
    print("After deleting number 10: ", numbers_tree.in_order_traversal())

    print("with my fullname: ")
    name_tree = build_tree(["V", "E", "N", "U", "S", "M", "D", "O", "N", "A", "S", "C", "O"])
    print("\nIn order traversal: ", name_tree.in_order_traversal())
    name_tree.delete("V")
    print("After deleting letter A: ", name_tree.in_order_traversal())
    name_tree.delete("M")
    print("After deleting letter M: ", name_tree.in_order_traversal())
    name_tree.delete("D")
    print("After deleting letter D: ", name_tree.in_order_traversal())

