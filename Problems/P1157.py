"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
"""


"""
내 풀이... 예제는 정답이였지만 결론적으로 틀림... 어느 부분에서 틀렸는지는 모르겠지만 정답을 보니 접근 방법 자체가 틀린것 같음....
import collections

str = input().upper()
count = collections.Counter(str)

result = ""
val = 0
for i in count.keys():
    if val < count[i]:
        val = count[i]
        result = i
    elif val == count[i]:
        result = "?"
        break
    else:
        continue

print(result)
"""



words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])

