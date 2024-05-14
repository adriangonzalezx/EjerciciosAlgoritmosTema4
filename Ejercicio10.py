class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes_in_level(root, level):
    if root is None:
        return 0
    if level == 0:
        return 1
    return count_nodes_in_level(root.left, level-1) + count_nodes_in_level(root.right, level-1)

def is_level_complete(root, level):
    if root is None:
        return False
    if level == 0:
        return True
    if level == 1:
        return root.left is not None and root.right is not None
    return is_level_complete(root.left, level-1) and is_level_complete(root.right, level-1)

def count_missing_nodes(root, level):
    if root is None:
        return 0
    if level == 0:
        return 0
    if level == 1:
        if root.left is None:
            return 1
        if root.right is None:
            return 1
        return 0
    return count_missing_nodes(root.left, level-1) + count_missing_nodes(root.right, level-1)

# Example usage
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# Calculate the number of nodes in a specific level
level = 2
num_nodes = count_nodes_in_level(root, level)
print(f"Number of nodes in level {level}: {num_nodes}")

# Check if a level is complete
is_complete = is_level_complete(root, level)
print(f"Level {level} is complete: {is_complete}")

# Count the number of missing nodes in a level
missing_nodes = count_missing_nodes(root, level)
print(f"Number of missing nodes in level {level}: {missing_nodes}")
