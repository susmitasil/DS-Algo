class BinaryNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data :
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryNode(data)

    def inorder_traversal(self):
        # print(self.data, end=" ")
        elements = []

        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def preorder_traversal(self):
        # print(self.data, end=" ")
        elements = []

        elements.append(self.data)
        
        if self.left:
            elements += self.left.inorder_traversal()
        
        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def postorder_traversal(self):
        # print(self.data, end=" ")
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        
        if self.right:
            elements += self.right.inorder_traversal()

        elements.append(self.data)

        return elements

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

def build_tree(elements):
    root = BinaryNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.inorder_traversal())
    print(numbers_tree.preorder_traversal())
    print(numbers_tree.postorder_traversal())
    print(numbers_tree.search(200))