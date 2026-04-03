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

def merge_k_lists(lists):
    if not lists:
        return []
    
    while len(lists) > 1:
        merged_lists = []

        for i in range(0,len(lists),2):
            arr1 = lists[i]
            arr2 = lists[i+1] if i+1 < len(lists) else None
            merged_lists.append(merge_two_lists(arr1,arr2))
        lists =merged_lists
    return lists[0]


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

l1 = build_list([1, 3, 5])
l2 = build_list([2, 4, 6])
l3 = build_list([3, 6, 9])
l4 = build_list([0, 10, 11])

lists = [l1, l2, l3, l4]

merged = merge_k_lists(lists)
print_list(merged)