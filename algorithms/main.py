import insertion_sort

A = [5,3,66,12,89,2,3,13]

insertion_sort.insertionSort(A)

print("Sorted array is:")
for i in range(len(A)):
    print ("%d" % A[i])