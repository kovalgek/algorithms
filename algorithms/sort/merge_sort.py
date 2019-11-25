
def merge(A, p, q, r):

    n1 = q - p + 1
    n2 = r - q

    L = []
    R = []

    for i in range(n1):
        L.append(A[p + i])

    for j in range(n2):
        R.append(A[q + 1 + j])

    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0

    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)

A = [5,2,4,7,1,3,2,6]

mergeSort(A,0,len(A)-1)

print("Sorted array is:")
for i in range(len(A)):
    print ("%d" % A[i])


