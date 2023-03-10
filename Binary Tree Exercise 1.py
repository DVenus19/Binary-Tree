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

        #Lastly,visiting the node
        elements.append(self.data)

        return elements

    #performs pre order traversal of a binary tree
    def pre_order_traversal(self):
        elements = []

      # First visiting the node
        elements.append(self.data)

        #Next is visit the left side
        if self.left:
            elements += self.left.pre_order_traversal()

        #Finally,visit the right side
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements


def build_tree(elements):
    print("Building tree with these following elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers_tree = build_tree([5, 41, 3, 20, 19, 67, 10, 15, 78, 18, 33, 65, 89])
    print("Minimum element in the list: ",numbers_tree.find_min())
    print("Maximum element in the list: ", numbers_tree.find_max())
    print("Is there a number 19? ", numbers_tree.search(19))
    print("Is there a number 131? ", numbers_tree.search(131))
    print("Is there a number 72? ", numbers_tree.search(72))
    print("Total Value: ", numbers_tree.calculate_sum())
    print("\nIn order traversal: ", numbers_tree.in_order_traversal())
    print("Pre order traversal: ",numbers_tree.pre_order_traversal())
    print("Post order traversal: ", numbers_tree.post_order_traversal())


    print("\nFor the Fullname : ")
    name_tree = build_tree(["V", "E", "N", "U", "S", "M", "D", "O", "N", "A", "S", "C","O"])
    print("Minimum element in the list: ", name_tree.find_min())
    print("Maximum element in the list: ", name_tree.find_max())
    print("Is there a letter O in my fullname? ", name_tree.search("O"))
    print("Is there a letter B in my fullname ? ", name_tree.search("B"))
    print("Is there a letter V in my fullname ? ", name_tree.search("V"))
    print("\nIn order traversal: ", name_tree.in_order_traversal())
    print("Pre order traversal: ", name_tree.pre_order_traversal())
    print("Post order traversal: ", name_tree.post_order_traversal())

