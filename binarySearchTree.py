class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self, key):
        self.root = Node(key)


    def search(self, key):
        node = self.root
        while node:
            if node.key == key:
                print("Found!")
                return node
            elif node.key > key:
                node = node.left
            else:
                node = node.right
        return None


    def insert(self, key):
        node = self.root
        while node:
            parent = node
            if node.key == key:
                print("Data already exists.")
            elif node.key > key:
                node = node.left
                parent.left = Node(key)
            else:
                node = node.right
                parent.right = Node(key)
        

t = BinarySearchTree(4)
t.insert(3)
t.insert(5)
t.insert(1)
t.insert(7)
print(t.root.key)
print(t.root.right.key)
print(t.root.left.key)
    
            