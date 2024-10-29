class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node: Node, key):
        if key < node.key:
            if node.left:
                self._insert(node.left, key)
            else:
                node.left = Node(key)
        else:
            if node.right:
                self._insert(node.right, key)
            else:
                node.right = Node(key)

    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, node: Node):
        if node is None:
            return None
        while node.right:
            node = node.right
        return node.key
    
    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, node: Node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.key

    def sum_values(self):
        return self._sum_values(self.root)

    def _sum_values(self, node: Node):
        if node is None:
            return 0
        return node.key + self._sum_values(node.left) + self._sum_values(node.right)