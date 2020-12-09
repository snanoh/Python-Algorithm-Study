import collections
import re
from typing import List

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def most_common_word(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split()
                if word not in banned]

    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫번째 인덱스 리턴
    return counts.most_common(1)[0][0]


print(most_common_word(paragraph, banned))