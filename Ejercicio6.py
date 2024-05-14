class Jedi:
    def __init__(self, name, species, birth_year, lightsaber_color, ranking, masters):
        self.name = name
        self.species = species
        self.birth_year = birth_year
        self.lightsaber_color = lightsaber_color
        self.ranking = ranking
        self.masters = masters

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root is None:
            self.root = Node(key, data)
        else:
            self._insert_recursive(self.root, key, data)

    def _insert_recursive(self, node, key, data):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, data)
            else:
                self._insert_recursive(node.left, key, data)
        else:
            if node.right is None:
                node.right = Node(key, data)
            else:
                self._insert_recursive(node.right, key, data)

    def inorder_traversal(self):
        self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node):
        if node is not None:
            self._inorder_traversal_recursive(node.left)
            print(node.data)
            self._inorder_traversal_recursive(node.right)

    def level_order_traversal(self):
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Create the access trees
name_tree = BinaryTree()
ranking_tree = BinaryTree()
species_tree = BinaryTree()

# Example usage
jedi1 = Jedi("Yoda", "Unknown", 896, "Green", "Jedi Master", ["Unknown"])
jedi2 = Jedi("Luke Skywalker", "Human", 19, "Blue", "Jedi Knight", ["Yoda"])
jedi3 = Jedi("Obi-Wan Kenobi", "Human", 57, "Blue", "Jedi Master", ["Qui-Gon Jinn"])
jedi4 = Jedi("Anakin Skywalker", "Human", 41, "Blue", "Jedi Knight", ["Obi-Wan Kenobi"])

name_tree.insert(jedi1.name, jedi1)
name_tree.insert(jedi2.name, jedi2)
name_tree.insert(jedi3.name, jedi3)
name_tree.insert(jedi4.name, jedi4)

ranking_tree.insert(jedi1.ranking, jedi1)
ranking_tree.insert(jedi2.ranking, jedi2)
ranking_tree.insert(jedi3.ranking, jedi3)
ranking_tree.insert(jedi4.ranking, jedi4)

species_tree.insert(jedi1.species, jedi1)
species_tree.insert(jedi2.species, jedi2)
species_tree.insert(jedi3.species, jedi3)
species_tree.insert(jedi4.species, jedi4)

# Perform operations on the trees
print("Inorder traversal by name:")
name_tree.inorder_traversal()

print("Inorder traversal by ranking:")
ranking_tree.inorder_traversal()

print("Level order traversal by ranking:")
ranking_tree.level_order_traversal()

print("Level order traversal by species:")
species_tree.level_order_traversal()
