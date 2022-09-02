class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            node = self.root
            while node.data:
                if data < node.data:
                    if node.left is None:
                        node.left = Node(data)
                        return self
                    # elif node.right is None:
                    #     node.right = Node(data)
                    #     return self
                    # else:
                    node = node.left
                else:
                    if node.right is None:
                        node.right = Node(data)
                        return self
                    # elif node.left is None:
                    #     node.left = Node(data)
                    #     return self
                    # else:
                    node = node.right

    def lookup(self, data):
        if data == self.root.data:
            return self.root
        else:
            node = self.root
            while node:
                if data < node.data:
                    node = node.left
                elif data > node.data:
                    node = node.right
                elif data == node.data:
                    return node
        return False


tree = BinarySearchTree()
tree.insert(9)
tree.insert(50)
tree.insert(60)
tree.insert(45)
tree.insert(6)
tree.insert(4)
tree.insert(7)

print(tree.lookup(6).right.data)
