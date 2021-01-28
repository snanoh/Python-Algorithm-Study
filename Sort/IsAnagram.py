

def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

s = "anagram"

t = "nagaram"

print(isAnagram(s,t))