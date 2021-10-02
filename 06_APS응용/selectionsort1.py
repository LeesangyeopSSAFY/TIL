def SelectionSort(A, st):
    if st == len(A) - 2:
        return A
    else:
        mini = st
        for i in range(st+1, len(A)):
            if A[i] < A[mini]:
                mini = i
        A[mini], A[st] = A[st], A[mini]
        return SelectionSort(A, st+1)

A = [3, 5, 2, 6, 1, 7, 8, 10, 56, 34, 12, 99]
ans = SelectionSort(A, 0)
print(ans)