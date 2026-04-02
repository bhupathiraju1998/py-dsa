class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 🔹 Function to reverse subpart
def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # move prev to node before 'left'
    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next

    # reverse sublist
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next


# 🔹 INPUT (you can change this)
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# 🔹 CALL FUNCTION (change left & right here)
head = reverseBetween(head, 2, 4)

# 🔹 PRINT OUTPUT
curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")