import collections
import re
from typing import Deque

string = "A man, a plan, a canal: Panama"


def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():  # 알파벳과 숫자일 경우에만
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def isPalindrome2(s: str) -> bool:
    """
    자료형 데크로 선언
    Deque란 양쪽에서 데이터를 가져올 수 있는 Queue
    """
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():  # Deque라서 popleft를 사용할 수 있음
            return False

    return True

def isPalindrome3(s: str) -> bool:
    s = s.lower() # 소문자로 전환
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)
    print(s[::-1])
    return s == s[::-1] #revers()

print(isPalindrome(string))
print(isPalindrome2(string))
print(isPalindrome3(string))