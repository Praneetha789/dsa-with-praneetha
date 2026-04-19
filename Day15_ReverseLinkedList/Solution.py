class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # store next
        curr.next = prev        # reverse link
        prev = curr             # move prev
        curr = next_node        # move curr

    return prev


# Example usage
# Creating list: 1 → 2 → 3 → 4 → 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reverse
new_head = reverse_list(head)

# Print result
curr = new_head
while curr:
    print(curr.val, end=" → ")
    curr = curr.next