class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1,l2):
    dummyNode = ListNode(-1)
    current = dummyNode 

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    return dummyNode.next 

def getMid(list:ListNode):
    slow,fast = list,list.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def sortList(head:ListNode)->ListNode:
    if not head or not head.next:
        return head
    
    # split the list into 2 halfs
    left = head
    right = getMid(head)
    tmp = right.next
    right.next = None
    right = tmp

    left = sortList(left)
    right = sortList(right)
    return merge_two_lists(left,right)




    


def build_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

l1 = build_list([4,2,1, 3, 5])



merged = sortList(l1)
print_list(merged)