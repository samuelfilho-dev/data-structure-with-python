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