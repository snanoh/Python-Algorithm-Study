# Phython Test
from typing import List

# 리스트 컴프리헨션


print(list(map(lambda x: x + 10, [1, 2, 3])))

print([n * 2 for n in range(1, 10 + 1) if n % 2 == 1])


# 제터레이터
def get_natural_number():
    n = 0
    # while로 무한히 수를 생성
    while True:
        n += 1
        yield n


g = get_natural_number()
# for문으로 next를 불러옴
for _ in range(0, 100):
    print(next(g))

# enumerate
a = [1, 2, 3, 4, 5, 6]
print(list(enumerate(a)))
for i, v in enumerate(a):
    print(i, v)

# print
idx = 1
fruit = "Apple"
print('{0}:{1}'.format(idx + 1, fruit))
print('{}: {}'.format(idx + 1, fruit))
print(f'{idx + 1}: {fruit}')


# test
def num_matching_subseq(S: str, words: List[str]) -> int:
    matched_count = 0

    for word in words:
        pos = 0
        for i in range(len(word)):
            found_pos = S[pos:].find(word[i])
            if found_pos < 0:
                matched_count -= 1
                break
            else:
                pos += found_pos + 1
        matched_count += 1

    return matched_count


arr = ['string', 'ring', 'ami', 'naver','tr']
print(num_matching_subseq("str", arr))


if_test = 0

if not (1 == if_test):
    print('gg')