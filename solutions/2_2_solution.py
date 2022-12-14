class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None

    def insert_head(self, value):
        new_node = LinkedList.Node(value)
        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    
    def remove_head(self):
        if self.head == self.tail:
            self.head = None
        elif self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next
        if self.head:
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = None
    
class Stack:
    def __init__(self):
        self.__data = LinkedList()
        self._num_elements = 0

    def push(self, value):
        self.__data.insert_head(value)
        self._num_elements += 1

    def pop(self):
        popped_head = None
        if self._num_elements:
            popped_head = self.__data.head.data
            self.__data.remove_head()
            self._num_elements -= 1
        return popped_head
    
    def size(self):
        return self._num_elements

    def empty(self):
        return not self.size()

linked_stack = Stack()
print(linked_stack.size())
print(linked_stack.empty())
linked_stack.push('D')
linked_stack.push('B')
linked_stack.push('A')
print(linked_stack.size())
print(linked_stack.empty())
print(linked_stack.pop())
print(linked_stack.pop())
linked_stack.push('C')
print(linked_stack.pop())
print(linked_stack.pop())
print(linked_stack.size())
print(linked_stack.empty())