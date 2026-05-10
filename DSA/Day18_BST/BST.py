class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert Node
    def insert(self, root, key):

        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self.insert(root.left, key)

        elif key > root.data:
            root.right = self.insert(root.right, key)

        return root

    # Search Node
    def search(self, root, key):

        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Inorder Traversal
    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


# Main Program
tree = BST()

tree.root = tree.insert(tree.root, 50)
tree.insert(tree.root, 30)
tree.insert(tree.root, 70)
tree.insert(tree.root, 20)
tree.insert(tree.root, 40)

print("Inorder Traversal:")
tree.inorder(tree.root)

found = tree.search(tree.root, 40)

print("\nSearch 40:", found)