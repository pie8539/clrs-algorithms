def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # insert A[j] into sorted list
        i = j-1
        while i>=00 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    return A

print(insertion_sort([120,90,6,2]))
