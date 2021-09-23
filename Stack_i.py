import random


# Stack is a classic data structure marked by its last-in, first-out feature,and thus
# its unique operations: pop() and push().
# Linked list can easily construct a stack.
class MyLinkedList:
    def __init__(self, next_node=None, value=None):
        self.next_node = next_node
        self.value = value

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

    def set_next_node(self, next_node):
        self.next_node = next_node

    def set_value(self, value):
        self.value = value

    # In the context of a linked list, the push() function simply means adding a node at
    # the beginning of the current list.
    def push(self, new_value):
        new_node = MyLinkedList()
        new_node.set_value(new_value)
        new_node.set_next_node(self.get_next_node())
        self.set_next_node(new_node)

    # Likewise, pop() means returning and deleting the first node in the list.
    def pop(self):
        if self.get_next_node() is not None:
            result = self.get_next_node()
            self.set_next_node(self.get_next_node().get_next_node())
            return result

    def length(self):
        cursor = self
        index = 0
        while cursor.get_next_node() is not None:
            index += 1
            cursor = cursor.get_next_node()
        return index

    def is_empty(self):
        if self.get_next_node() is None:
            return True
        return False

    def peek(self):
        if self.get_next_node() is not None:
            return self.get_next_node().get_value()


# Stacks can provide another solution to sorting problems. The following function takes a
# stack and sorts it.
def stack_insertion_sort(items):
    # A temporary stack
    temp_stack = MyLinkedList()
    while items.is_empty() is False:
        # locate next entry
        # pop and acquire first entry in the stack
        temp = items.pop().get_value()
        # if the temporary stack is not empty and the first item in temp is greater than the
        # first item in the original stack
        while temp_stack.is_empty() is False and temp_stack.peek() > temp:
            # move the larger value to the top of original stack
            items.push(temp_stack.peek())
            temp_stack.pop()
        temp_stack.push(temp)
    return temp_stack


def print_list(node):
    while node is not None:
        print(node.get_value())
        node = node.get_next_node()


test_stack = MyLinkedList()
for i in range(0, 6):
    test_stack.push(random.randint(1, 10))
print_list(test_stack)
print("________________________")
print_list(stack_insertion_sort(test_stack))
