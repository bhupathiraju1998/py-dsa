class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 🔹 Function to find middle
def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# 🔹 INPUT
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# 🔹 CALL FUNCTION
mid = middleNode(head)

# 🔹 PRINT ORIGINAL LIST (don't destroy head)
curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")

# 🔹 PRINT MIDDLE
print("Middle node value:", mid.val)