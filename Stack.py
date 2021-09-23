class MyStack:
    def __init__(self, next_node=None, value=None):
        self.next_node = next_node
        self.value = value

    # In the context of a linked list, the push() function simply means adding a node at
    # the beginning of the current list.
    def push(self, new_value):
        new_node = MyStack()
        new_node.value = new_value
        new_node.next_node = self.next_node
        self.next_node = new_node

    # Likewise, pop() means returning and deleting the first node in the list.
    def pop(self):
        if self.next_node is not None:
            result = self.next_node
            self.next_node = self.next_node.next_node
            return result

    def length(self):
        cursor = self
        index = 0
        while cursor.next_node is not None:
            index += 1
            cursor = cursor.next_node
        return index

    def is_empty(self):
        if self.next_node is None:
            return True
        return False

    def peek(self):
        if self.next_node is not None:
            return self.next_node.value
