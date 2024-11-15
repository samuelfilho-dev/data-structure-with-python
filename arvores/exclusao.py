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

    # Caso Medio: O ( log n)
    # Pior Caso: O(n)
    def search(self, key):
        current = self.root
        while current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
            if current is None:
                return None
        return current

    def order(self, node):
        if node is not None:
            self.order(node.left)
            print(node.key)
            self.order(node.right)

    def delete(self, key):
        if self.root is None:
            print('A Arvore está Vazia')

        current = self.root
        parent = self.root
        is_left = True
        while current.key != key:
            parent = current
            # Esquerda
            if key < current.key:
                is_left = True
                current = current.left
            else:
                is_left = False
                current = current.right
            if current is None:
                return False

        # O Nó a ser apagado é uma folha
        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            elif is_left:
                parent.left = None
            else:
                parent.right = None

        # Nó a ser apagado não possui um filho na direita
        elif current.right is None:
            if current == self.root:
                self.root = current.left
            elif is_left:
                parent.left = current.left
            else:
                parent.right = current.left

        # Nó a ser apagado não possui um filho na esquerda
        elif current.left is None:
            if current == self.root:
                self.root = current.right
            elif is_left:
                parent.left = current.right
            else:
                parent.right = current.right

        # Nó possui dois filhos
        else:
            successor = self.get_successor(current)
            if current == self.root:
                self.root = successor
            elif is_left:
                parent.left = successor
            else:
                parent.right = successor

            successor.left = current.left

        return True

    def get_successor(self, node):
        parent_successor = node
        successor = node
        current = node.right
        while current is not None:
            parent_successor = successor
            successor = current
            current = current.left

        if successor != node.right:
            parent_successor.left = successor.right
            successor.right = node.right

        return successor


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

# tree.delete(9)
# tree.delete(79)

# tree.delete(84)
# tree.delete(9)
# tree.delete(14)

tree.delete(72)

tree.order(tree.root)
