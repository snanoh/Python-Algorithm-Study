from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None



def sortList(head: ListNode) -> ListNode:
    # 연결 리스트 -> 파이썬 리스트
    p = head
    lst: List = []
    while p:
        lst.append(p.val)
        p = p.next

    # 정렬
    lst.sort()

    # 파이썬 리스트 -> 연결 리스트
    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next
    return head



