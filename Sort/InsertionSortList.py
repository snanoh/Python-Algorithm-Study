
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def add(head, val):
    if head is None:
        head = ListNode(val)
    else:
        node = head
        while node.next:
            node = node.next
        node.next = ListNode(val)

def desc(head):
    node = head
    while node:
        print(node.val)
        node = node.next


list = [4 ,2 ,1 ,3]
head = ListNode(list[0])
for i in list[1:]:
    add(head, i)

def insert_sort_list(head: ListNode) -> ListNode:
    cur = parent = ListNode(0)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next

        #필요한 경우에만 cur 포인터가 되돌아가도록 처리
        if head and cur.val > head.val:
            cur = parent
    return parent.next


desc(insert_sort_list(head))