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

    def _remove_target_node(self, node):
        # Some status flagging
        has_parent = None
        is_left_child = None

        if not node.parent:
            has_parent = False
            is_left_child = False
        else:
            has_parent = True
            if node != node.parent.left:
                is_left_child = False
            else:
                is_left_child = True

        # main conditionals
        if not node.left and not node.right:
            if not has_parent:
                self.root = None
            else:
                if is_left_child:
                    node.parent.left = None
                else:
                    node.parent.right = None
        
        if node.left and not node.right:
            if not has_parent:
                self.root = node.left
                node.left.parent = node.parent
            else:
                if is_left_child:
                    node.parent.left = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.right = node.left
                    node.left.parent = node.parent

        if node.right and not node.left:
            if not has_parent:
                self.root = node.right
                node.right.parent = node.parent
            else:
                if is_left_child:
                    node.parent.left = node.right
                    node.right.parent = node.parent

                else:
                    node.parent.right = node.right
                    node.right.parent = node.parent

        # the monstrous double child scenario
        if node.right and node.left:
            # Locate the successor node
            successor = node.right
            while successor.left:
                successor = successor.left
            
            # if successor node is node.right,
            #   simply slide it into place
            if successor == node.right:
                # move successor
                successor.left = node.left
                node.left.parent = successor

                # handle old node's parent
                successor.parent = node.parent

                if not has_parent:
                    # new root scenario
                    self.root = successor
                else:
                    if is_left_child:
                        node.parent.left = successor
                    else:
                        node.parent.right = successor
                    
            # Otherwise, links will have to be broken
            #   around the successor, and some housekeeping
            #   is in order before moving the successor
            #   to its now location in the BST
            else:
                # Handle Successor's Right child (if any).
                #   No left child is possible as the successor
                #   is the leftmost child on that subtree
                successor.parent.left = successor.right # May be None
                if successor.right:
                    successor.right.parent = successor.parent
                
                # Move the Successor into place
                successor.left = node.left
                successor.left.parent = successor
                successor.right = node.right
                successor.right.parent = successor
                # handle old node's parent
                successor.parent = node.parent
                if not has_parent:
                    # new root scenario
                    self.root = successor
                else:
                    if is_left_child:
                        successor.parent.left = successor
                    else:
                        successor.parent.right = successor

    def remove(self, value):
        # Write me!
        #   you should use (but not have to change) the
        #   self._remove_target_node() method defined above
        if not self.root:
            return

        target_node = self._find_remove(value, self.root)
        if target_node:
            self._remove_target_node(target_node)


    def _find_remove(self, data, node):
        # Write me!
        #   Recursively fetch the node itself first so you can then remove it
        #   similar to self._contains()
        if not node:
            return None
        elif data == node.data:
            return node
        elif data < node.data:
            return self._find_remove(data, node.left)
        else:
            return self._find_remove(data, node.right)

acceptance_list = BST()
acceptance_list.insert("Daniel Loveday")
acceptance_list.insert("Barns, Nathan")
acceptance_list.insert("Ayns, Georgia")
acceptance_list.insert("Charles, Samantha")
acceptance_list.insert("Sanders, Alex")
acceptance_list.insert("Puck, Kyle")
acceptance_list.insert("Washburn, Rebecca")
# oops
acceptance_list.remove("Daniel Loveday")
acceptance_list.remove("Nathan Barns")
acceptance_list.insert("Loveday, Daniel")
acceptance_list.insert("Barns, Nathan")

for x in acceptance_list:
    print(x)