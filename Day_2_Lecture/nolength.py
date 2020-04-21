class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
four = Node(4)
three = Node(3, four)
two = Node(2, three)
one = Node(1, two)
head_node = Node(0, one)
def find_middle(head):
    fast_pointer = head
    slow_pointer = head
    while fast_pointer.next is not None:
        fast_pointer = fast_pointer.next
        if fast_pointer.next is None:
            return slow_pointer
        fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next
    return slow_pointer
print(find_middle(head_node).value)