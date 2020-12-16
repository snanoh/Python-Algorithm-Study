from typing import List


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


list = [1 ,2 ,3 ]
list2 = [4 ,5 ,6 ]
head = ListNode(list[0])
for i in list[1:]:
    add(head, i)

head2 = ListNode(list2[0])
for i in list2[1:]:
    add(head2, i)

class Solution:
    #연결 리스트 뒤집기
    def reverse_list(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def to_list(self, node: ListNode) -> ListNode:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    #파이썬 리스트를 연결 리스트로 변환
    def to_reversed_linked_list(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
    
    #두 연결 리스트의 덧셈
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.to_list(self.reverse_list(l1))
        b = self.to_list(self.reverse_list(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))

        #최종 계산 결과 연결 리스트 변환
        return self. to_reversed_linked_list(str(resultStr))


sol = Solution()
desc(sol.add_two_numbers(head, head2))


