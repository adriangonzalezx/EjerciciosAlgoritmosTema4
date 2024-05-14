class Node:
    def __init__(self, name, is_hero):
        self.name = name
        self.is_hero = is_hero
        self.left = None
        self.right = None

def insert(root, name, is_hero):
    if root is None:
        return Node(name, is_hero)
    if name < root.name:
        root.left = insert(root.left, name, is_hero)
    elif name > root.name:
        root.right = insert(root.right, name, is_hero)
    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.name)
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root:
        print(root.name)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.name)

def find_node(root, name):
    if root is None or root.name == name:
        return root
    if name < root.name:
        return find_node(root.left, name)
    return find_node(root.right, name)

def modify_node(root, name, new_name):
    node = find_node(root, name)
    if node:
        node.name = new_name

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def create_forest(root):
    heroes_root = None
    villains_root = None
    current = root
    while current:
        if current.is_hero:
            heroes_root = insert(heroes_root, current.name, True)
        else:
            villains_root = insert(villains_root, current.name, False)
        current = current.right
    return heroes_root, villains_root

def count_tree_nodes(root):
    if root is None:
        return 0
    return 1 + count_tree_nodes(root.left) + count_tree_nodes(root.right)

def alphabetical_traversal(root):
    if root:
        alphabetical_traversal(root.left)
        print(root.name)
        alphabetical_traversal(root.right)

# Create the tree
root = None
root = insert(root, "Iron Man", True)
root = insert(root, "Captain America", True)
root = insert(root, "Thor", True)
root = insert(root, "Hulk", True)
root = insert(root, "Black Widow", True)
root = insert(root, "Hawkeye", True)
root = insert(root, "Black Panther", True)
root = insert(root, "Doctor Strange", False)
root = insert(root, "Loki", False)
root = insert(root, "Thanos", False)

# List villains alphabetically
villains_root = create_forest(root)[1]
alphabetical_traversal(villains_root)

# List superheroes starting with C
def superheroes_starting_with_C(root):
    if root:
        superheroes_starting_with_C(root.left)
        if root.name.startswith("C"):
            print(root.name)
        superheroes_starting_with_C(root.right)
superheroes_starting_with_C(root)

# Count superheroes in the tree
print(count_nodes(root))

# Modify Doctor Strange's name
modify_node(root, "Doctor Strange", "Doctor Strange")

# List superheroes in descending order
def superheroes_descending_order(root):
    if root:
        superheroes_descending_order(root.right)
        print(root.name)
        superheroes_descending_order(root.left)
superheroes_descending_order(root)

# Create the forest
heroes_root, villains_root = create_forest(root)

# Count nodes in each tree
print(count_tree_nodes(heroes_root))
print(count_tree_nodes(villains_root))

# Alphabetical traversal of each tree
alphabetical_traversal(heroes_root)
alphabetical_traversal(villains_root)
