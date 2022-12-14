class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.parent = None
            self.left = None
            self.right = None
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data == node.data:
            return
        elif data < node.data:
            if not node.left:
                node.left = BST.Node(data)
                node.left.parent = node
            else:
                self._insert(data, node.left)
        else:
            if not node.right:
                node.right = BST.Node(data)
                node.right.parent = node
            else:
                self._insert(data, node.right)
    
    def __contains__(self, data):
        return self._contains(data, self.root)

    def _contains(self, data, node):
        if not node:
            return False
        elif data == node.data:
            return True
        elif data < node.data:
            return self._contains(data, node.left)
        else:
            return self._contains(data, node.right)

    def __iter__(self):
        yield from self._traverse_forward(self.root)

    def _traverse_forward(self, node):
        if node:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
    
    def __reversed__(self):
        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):
        if node:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self):
        if not self.root:
            return 0
        else:
            return self._get_height(self.root)

    def _get_height(self, node):
        if not node:
            return 0
        else:
            return max(self._get_height(node.left), self._get_height(node.right)) + 1

