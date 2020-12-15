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


list = [1 ,2 ,3 ,4 ,5]
head = ListNode(list[0])
for i in list[1:]:
    add(head, i)


def reverseList( head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)

print(desc(reverseList(head)))