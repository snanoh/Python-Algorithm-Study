"""J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇개 나 있을까? 대소문자는 구분한다."""
import collections

J="aA"
S = "aAAbbbb"


def num_jewels_in_stoens(J: str, S: str) -> int:
    freqs = {}
    count = 0
    
    #돌(S)의 빈도 수 계산
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    #보석(J)의 빈도 수 합산
    for char in J:
        if char in freqs:
            count += freqs[char]

    return count

print(num_jewels_in_stoens(J,S))

#use defaultdict
def num_jewels_in_stoens2(J: str, S: str) -> int:
    freqs = collections.defaultdict(int)
    count = 0

    #비교 없이 돌(S) 빈도 수 계산
    for char in S:
        freqs[char] += 1

    #비교 없이 보석(J) 빈도수 합산
    for char in J:
        count += freqs[char]

    return count

print(num_jewels_in_stoens2(J,S))

#use counter
def num_jewels_in_stoens2(J: str, S: str) -> int:
    freqs = collections.Counter(S) #돌(S)의 빈도 수 계산
    count = 0

    #비교 없이 보석(J) 빈도 수 합산
    for char in J:
        count += freqs[char]

    return count

#Python 풀이
def num_jewels_in_stoens4(J: str, S: str) -> int:
    return sum(s in J for s in S)

print(num_jewels_in_stoens4(J,S))