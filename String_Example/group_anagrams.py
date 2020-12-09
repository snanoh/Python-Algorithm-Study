import collections
from typing import List

test = ["eat", "tea", "ate", "tan", "nat", "bat"]

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list) #list를 담을 수 있는 list를 만듬

    for word in strs:
        #정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values();


print(group_anagrams(test))


