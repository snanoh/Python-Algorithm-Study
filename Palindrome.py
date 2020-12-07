string = "A man, a plan, a canal: Panama"

def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            str.append(char.lower())

        #팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

def isPalindrome2(s: str) -> bool:
    pass