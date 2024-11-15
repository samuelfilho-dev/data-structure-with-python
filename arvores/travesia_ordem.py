# Forma Recursiva
# Esquerda,Raiz,Direita
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def show_node(self):
        print(self.key)


class SearchBinaryTree:
    def __init__(self):
        self.root = None

    # Caso Medio: O ( log n)
    # Pior Caso: O(n)
    def insert(self, key):
        new = Node(key)

        if self.root is None:
            self.root = new
        else:
            current = self.root
            while True:
                parent = current
                # Esquerda
                if key < current.key:
                    current = current.left
                    if current is None:
                        parent.left = new
                        return
                # Direita
                else:
                    current = current.right
                    if current is None:
                        parent.right = new
                        return

    def order(self, node):
        if node is not None:
            self.order(node.left)
            print(node.key)
            self.order(node.right)

tree = SearchBinaryTree()

tree.insert(53)
tree.insert(30)
tree.insert(14)
tree.insert(39)
tree.insert(9)
tree.insert(23)
tree.insert(34)
tree.insert(49)
tree.insert(72)
tree.insert(61)
tree.insert(84)
tree.insert(79)

tree.order(tree.root)