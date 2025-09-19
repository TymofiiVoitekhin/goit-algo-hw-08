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

def nodes_sum (node: Node):
    sum = 0

    if node.left is None and node.right is None:
        sum += node.val

    elif node.left is None and node.right is not None:
        sum += node.val + nodes_sum(node.right)
    
    elif node.left is not None and node.right is None:
        sum += node.val + nodes_sum(node.left)

    else:
        sum += nodes_sum(node.left) + nodes_sum(node.right) + node.val
    
    return sum
    

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

print("Сума всіх вузлів:", nodes_sum(root))