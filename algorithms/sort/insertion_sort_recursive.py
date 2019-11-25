
def insertionSortRecursive(A, n):

    if n <= 1:
        return

    insertionSortRecursive(A, n - 1)

    key = A[n-1]
    i = n - 2
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i = i - 1
    A[i+1] = key


A = [5,3,66,12,89,2,3,13]

insertionSortRecursive(A, len(A))

print("Sorted array is:")
for i in range(len(A)):
    print ("%d" % A[i])