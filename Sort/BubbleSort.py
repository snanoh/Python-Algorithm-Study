


def bubblesort(A):
    for i in range(1, len(A)):
        for j in range(0, len(A) -1 ):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

print(bubblesort([5,12,4,32,6,1]))