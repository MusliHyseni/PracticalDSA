# Implementation of linked list in Python

# Node class. Used for creating a new node
class Node:
    def __init__(self, data=None, _next=None):
        self.data = data
        self._next = _next
    
# Linked list implementation 
class linked_list:
    def __init__(self):
# The head is inititalized as None, because we have an empty linked list
        self.head = None
        
# Static sequence interface operations

    # Length of linked list - O(n)
    def __len__(self):
            length = 0
            if self.head is None:
                return length
            iterator = self.head
            while iterator is not None:
                iterator = iterator._next
                length += 1
            return length

    # Insert node with data x, at the end - O(n)
    def insert_last(self, x):
            x_node = Node(x)
            if self.head is None:
                self.head = x_node
            iterator = self.head
            while iterator._next is not None:
                iterator = iterator._next
            iterator._next = x_node
            
            
    # Delete last node - O(n)
    def delete_last(self):
        if self.head is None:
            raise SyntaxError('Can not perform operation "delete_last" on empty linked list!')
        # First way of implementing: looking two steps ahead
        iterator = self.head
        while iterator._next._next is not None:
            iterator = iterator._next
        iterator._next = None
        
        
# Dynamic sequence interface operations
    def insert_first(self, x):
        prev = self.head
        node = Node(x, self.head)
        self.head = node
        self.head._next = prev