
def binarySearch(A, x):

    left = 0
    right = len(A) - 1
    mid = 0

    while True:

        mid = (left + right) // 2

        if x > A[mid]:
            mid = mid + 1
            left = mid
        if x < A[mid]:
            mid = mid - 1
            right = mid

        if A[mid] == x or left >= right:
            break

    return mid

A = [1, 4, 6, 8, 15, 35, 67, 199, 245, 567, 789, 1000]

mid = binarySearch(A, 1000)

print(mid)


