import collections
from typing import List, Deque


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def add(head, val):
    if head is None:
        head = Node(val)
    else:
        node = head
        while node.next:
            node = node.next
        node.next = Node(val)

list = [1 ,2 ,2 ,1]
head = Node(list[0])
for i in list[1:]:
    add(head, i)



def is_palindrome(head: Node) -> bool:
    q: List = []

    if not head:
        return True
    
    node = head
    
    #리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    #팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


#데크 풀이
def is_palindrome2(head: Node) -> bool:
    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next


    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True

def is_palindrome3(head: Node) -> bool:
    rev = None
    slow = fast = head
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    #팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev



print(is_palindrome(head))
print(is_palindrome2(head))
print(is_palindrome3(head))
