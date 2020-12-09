from typing import List

logs = ["dig1 8 1 5 1", "leg1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


def reorder_log_files(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit(): #숫자일 경우
            digits.append(log)
        else:
            letters.append(log)

    # 2두개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    digits.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


print(reorder_log_files(reorder_log_files(logs)))