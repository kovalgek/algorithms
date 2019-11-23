
def selectionSort(A):
    for j in range(0, len(A)-1):
        minIndex = j
        for i in range(j+1, len(A)):
            if A[i] < A[minIndex]:
                minIndex = i
        temp = A[j]
        A[j] = A[minIndex]
        A[minIndex] = temp


A = [5,3,66,12,89,2,3,130,100]

selectionSort(A)

print("Sorted array is:")
for i in range(len(A)):
    print ("%d" % A[i])