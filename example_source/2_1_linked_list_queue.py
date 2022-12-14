class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value):
        new_node = LinkedList.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_tail(self, value):
        new_node = LinkedList.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def remove_head(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next
    
    def remove_tail(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.tail is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def insert_after(self, value, new_value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                if current_node == self.tail:
                    self.insert_tail(new_value)
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = current_node
                    new_node.next = current_node.next
                    current_node.next.prev = new_node
                    current_node.next = new_node
                return
            current_node = current_node.next
    
    def remove(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                if current_node == self.head:
                    self.remove_head()
                elif current_node == self.tail:
                    self.remove_tail()
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    del current_node
                return
            current_node = current_node.next
    
    def replace(self, old_value, new_value):
        current_node = self.head
        while current_node:
            if current_node.data == old_value:
                current_node.data = new_value
                return
            current_node = current_node.next
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __reversed__(self):
        current_node = self.tail
        while current_node:
            yield current_node.data
            current_node = current_node.prev

    def __str__(self):
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output


class Queue:
    def __init__(self):
        self.__data = LinkedList()

    def enqueue(self, value):
        # we're going to use the tail as the back of the line
        self.__data.insert_tail(value)

    def dequeue(self):
        # Similar to the stack's pop() function, the dequeue function
        #   simply needs to needs to remove and return the first item
        value = None
        if self.__data.head:
            # Needed to ensure we weren't trying to access a member variable
            #   of a null value, in case we tried to dequeue from an empty
            #   linked list.
            value = self.__data.head.data
            self.__data.remove_head()
        return value