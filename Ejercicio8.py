class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_min_node(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.value

def get_max_node(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.value

# Example usage
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

min_value = get_min_node(root)
max_value = get_max_node(root)

print("Minimum node value:", min_value)
print("Maximum node value:", max_value)
