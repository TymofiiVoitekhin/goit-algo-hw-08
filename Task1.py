class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Оскільки менші значення знаходяться зліва, то найменше значення буде на рівні листків першим
def search_min_value (node: Node):

    if node.left:
       min_value = search_min_value(node.left)
    else:
        min_value = node.val
        return print("Мінімальне значення дерева:", min_value)


# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

search_min_value(root)