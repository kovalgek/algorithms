
def linearSearch(A, x):
    for i in range(len(A)):
        if x == A[i]:
            return i
    return None

A = [54, 6, 12, 3, 1, 7, 9, 54, 100, 9]

index = linearSearch(A, 7)

print("i=%d" % index)