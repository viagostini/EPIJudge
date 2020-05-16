def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]

    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
    
    return A

def dutch_flag_partition2(pivot_index, A):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    
    ans = ([0] * count[0])
    ans.extend([1] * count[1])
    ans.extend([2] * count[2])
    return ans


a = [2, 2, 0, 2]
print(dutch_flag_partition(2, a))
print(dutch_flag_partition2(2, a))