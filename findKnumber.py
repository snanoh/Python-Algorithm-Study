def solution(array, commands):
    answer = []

    for arr in commands:
        temp_arr = []  # 임시 생성
        for j in array[arr[0]-1:arr[1]]:  # 받은 array 담기
            temp_arr.append(j)

        temp_arr.sort()
        answer.append(temp_arr[arr[2]-1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
