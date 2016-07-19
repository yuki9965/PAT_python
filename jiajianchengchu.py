import math
def count( A, n):
    # write code here
    left = 0
    right = n-1
    count = 0
    while(left!=right and abs(left-right) != 1):
        if A[left]>A[left+1]:
            count += 1
        if A[right]<A[right-1]:
            count += 1

        left += 1
        right -= 1

    return count

print count([1,2,3,4,5,6,7,0],8)