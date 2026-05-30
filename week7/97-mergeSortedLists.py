import heapq

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    heap = []

    # push first node of each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))#heap arg → the list that is acting as a heap

    dummy = ListNode()
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap) #always remvoes the smallest, in heap the samll is always the root 

        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


# --------------------------
# Helper functions
# --------------------------

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    temp = head
    for x in arr[1:]:
        temp.next = ListNode(x)
        temp = temp.next
    return head


def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()


# --------------------------
# INPUT
# --------------------------

l1 = create_linked_list([1, 4, 7])
l2 = create_linked_list([2, 5, 8])
l3 = create_linked_list([3, 6, 9])

lists = [l1, l2, l3]

# --------------------------
# OUTPUT
# --------------------------

merged = mergeKLists(lists)

print("Merged Linked List:")
print_linked_list(merged)

# Companies like Google or Netflix collect logs from many servers:

# Server A logs (sorted by timestamp)
# Server B logs
# Server C logs

# 👉 Need to merge into one global timeline




import heapq

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    heap = []

    # push first node of each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap)

        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


# --------------------------
# Helper functions
# --------------------------

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    temp = head
    for x in arr[1:]:
        temp.next = ListNode(x)
        temp = temp.next
    return head


def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()


# --------------------------
# INPUT
# --------------------------

l1 = create_linked_list([1, 4, 7])
l2 = create_linked_list([2, 5, 8])
l3 = create_linked_list([3, 6, 9])

lists = [l1, l2, l3]

# --------------------------
# OUTPUT
# --------------------------

merged = mergeKLists(lists)

print("Merged Linked List:")
print_linked_list(merged)

# | Step | Action    | Heap           | Popped | Result List | Heap Push |
# | ---- | --------- | -------------- | ------ | ----------- | --------- |
# | 0    | Init push | (1,L1), (2,L2) | -      | []          | -         |
# | 1    | pop       | (2,L2)         | 1      | [1]         | push 4    |
# | 2    | pop       | (4,L1), (3,L2) | 2      | [1,2]       | push 3    |
# | 3    | pop       | (4,L1)         | 3      | [1,2,3]     | -         |
# | 4    | pop       | empty          | 4      | [1,2,3,4]   | -         |
# pop will remove the smallest