class MyLinkedList:
    value = None
    next_node = None

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_value(self, value):
        self.value = value

    def set_next(self, node):
        self.next_node = node


def find_node(node, target):
    if node is None:
        return None
    while node.next_node is not None:
        if node.next_node.value == target:
            return node
        node = node.next_node
    return None


def add_after_head(node, value):
    added_node = MyLinkedList(value)
    added_node.set_next(node.next_node)
    node.set_next(added_node)


def add_after_target(node, target, value):
    added_node = MyLinkedList(value)
    target_node = find_node(node, target).next_node
    added_node.set_next(target_node.next_node)
    target_node.set_next(added_node)


def add_after_tail(node, value):
    added_node = MyLinkedList(value)
    while node.next_node is not None:
        node = node.next_node
    node.set_next(added_node)


def remove_target(node, target):
    target_node = find_node(node, target)
    target_node.set_next(target_node.next_node.next_node)


def print_list(node):
    while node is not None:
        print(node.value)
        node = node.next_node


def copy_head(old_head):
    new_head = MyLinkedList(None)
    last_added = new_head
    old_node = old_head.next_node
    while old_node is not None:
        last_added.set_next(MyLinkedList(None))
        last_added = last_added.next_node
        last_added.set_value(old_node.value)
        old_node = old_node.next_node
    last_added.set_next(None)
    return new_head


def insert_sort(old_head):
    # Create a sentinel for new (sorted) list
    new_head = MyLinkedList(None)
    new_head.set_next(None)
    # Skip the sentinel of the copied list
    old_head = old_head.next_node
    while old_head is not None:
        # Acquire next (to be sorted) node from old list
        next_node = old_head
        # Proceed old list
        old_head = old_head.next_node
        # Find the position for current node
        after_me = new_head
        while after_me.next_node is not None and after_me.next_node.value < next_node.value:
            after_me = after_me.next_node
        # Insert current node into sorted list
        next_node.set_next(after_me.next_node)
        after_me.set_next(next_node)
    return new_head


def selection_sort(old_head):
    # Create a sentinel for new (sorted) list
    new_head = MyLinkedList(None)
    new_head.set_next(None)
    # While: repeatedly process until old list is empty
    while old_head.next_node is not None:
        # Find largest value in old list
        # The best_after_me indicates the node BEFORE the largest node
        best_after_me = old_head
        best_value = best_after_me.next_node.value
        # Start checking next value
        after_me = old_head.next_node
        while after_me.next_node is not None:
            if after_me.next_node.value > best_value:
                best_after_me = after_me
                best_value = after_me.next_node.value
            after_me = after_me.next_node
        # Remove from the old list the node with largest value
        best_node = best_after_me.next_node
        best_after_me.set_next(best_node.next_node)
        # Add the node with largest value to the top of sorted list
        best_node.set_next(new_head.next_node)
        new_head.set_next(best_node)
    return new_head
