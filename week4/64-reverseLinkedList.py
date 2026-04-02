
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head:ListNode)->ListNode:
    prev,curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr 
        curr = nxt 
    return prev #curr head
# 🔹 INPUT (build linked list)
head = ListNode(1, ListNode(2, ListNode(3)))

# 🔹 CALL FUNCTION
new_head = reverseList(head)
curr = new_head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")