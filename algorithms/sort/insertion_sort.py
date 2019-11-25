# sorting array by insert sort algorithm
def insertionSort(A):
    for j in range(len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key


A = [5,3,66,12,89,2,3,13]

insertionSort(A)

print("Sorted array is:")
for i in range(len(A)):
    print ("%d" % A[i])