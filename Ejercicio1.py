import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance_factor = self.get_balance_factor(root)

        if balance_factor > 1:
            if data < root.left.data:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance_factor < -1:
            if data > root.right.data:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def delete(self, root, data):
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.get_min_node(root.right)
                root.data = min_node.data
                root.right = self.delete(root.right, min_node.data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance_factor = self.get_balance_factor(root)

        if balance_factor > 1:
            if self.get_balance_factor(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance_factor < -1:
            if self.get_balance_factor(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def search(self, root, data):
        if not root or root.data == data:
            return root
        elif data < root.data:
            return self.search(root.left, data)
        else:
            return self.search(root.right, data)

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance_factor(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_min_node(self, root):
        if root.left:
            return self.get_min_node(root.left)
        return root

    def pre_order_traversal(self, root):
        if root:
            print(root.data, end=" ")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.data, end=" ")
            self.in_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.data, end=" ")

    def level_order_traversal(self, root):
        if not root:
            return

        queue = []
        queue.append(root)

        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def get_subtree_height(self, root):
        if not root:
            return 0
        return root.height

    def get_element_count(self, root, data):
        count = 0
        if root:
            if root.data == data:
                count += 1
            count += self.get_element_count(root.left, data)
            count += self.get_element_count(root.right, data)
        return count

    def count_parity(self, root):
        even_count = 0
        odd_count = 0
        if root:
            if root.data % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
            even_count += self.count_parity(root.left)
            even_count += self.count_parity(root.right)
        return even_count, odd_count

# Generate 1000 random integers
numbers = random.sample(range(1, 10001), 1000)

# Create an AVL tree
avl_tree = AVLTree()
for number in numbers:
    avl_tree.root = avl_tree.insert(avl_tree.root, number)

# Perform the activities
print("Preorder Traversal:")
avl_tree.pre_order_traversal(avl_tree.root)
print("\n")

print("Inorder Traversal:")
avl_tree.in_order_traversal(avl_tree.root)
print("\n")

print("Postorder Traversal:")
avl_tree.post_order_traversal(avl_tree.root)
print("\n")

print("Level Order Traversal:")
avl_tree.level_order_traversal(avl_tree.root)
print("\n")

number_to_search = 42
if avl_tree.search(avl_tree.root, number_to_search):
    print(f"{number_to_search} is present in the tree")
else:
    print(f"{number_to_search} is not present in the tree")

numbers_to_delete = [10, 20, 30]
for number in numbers_to_delete:
    avl_tree.root = avl_tree.delete(avl_tree.root, number)

left_subtree_height = avl_tree.get_subtree_height(avl_tree.root.left)
right_subtree_height = avl_tree.get_subtree_height(avl_tree.root.right)
print(f"Height of the left subtree: {left_subtree_height}")
print(f"Height of the right subtree: {right_subtree_height}")

element_to_count = 5
element_count = avl_tree.get_element_count(avl_tree.root, element_to_count)
print(f"Number of occurrences of {element_to_count}: {element_count}")

even_count, odd_count = avl_tree.count_parity(avl_tree.root)
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
