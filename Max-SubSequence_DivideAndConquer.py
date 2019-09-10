from math import inf
def max_cross_subarray(A, low, mid, high):
    '''
    Helper function for computing maximal subarray that crosses the middle.
    Returns the 'low' and 'high' index and the sum of the best cross.
    Running time is O(2n*n)=O(n)
    '''
    # Starting from middle to low index, computes the best possible solution 
    left_sum = -inf
    sub_sum = 0
    for i in range(mid, low-1, -1):
        sub_sum += A[i]
        if sub_sum > left_sum:
            left_sum = sub_sum
            left_idx = i

    # Starting from middle to high index, computes the best possible solution.
    right_sum = -inf
    sub_sum = 0
    for i in range(mid+1, high+1, 1):
        sub_sum += A[i]
        if sub_sum > right_sum:
            right_sum = sub_sum
            right_idx = i
    
    return (left_idx, right_idx, left_sum+right_sum)
   
def max_subsequence(A, low, high):
    '''
    Divide and Conquer approach for computing the maximal subarray in an array with positive and negative values
    Bounded by O(log(n)*n)
    '''
    # Bottom of recursion when the 'low' and 'high' index is the same, i.e. only one element.
    if low == high:
        return (low, high, A[low])
    
    mid = int(((low+high)/2))
    
    # Divides the array into two halves and recursively computes the 
    # indices and sum that corresponds to the highest possible sum in the subarrays
    (left_low_idx, left_high_idx, left_sub_sum) = max_subsequence(A, low, mid)
    (right_low_idx, right_high_idx, right_sub_sum) = max_subsequence(A, mid+1, high)
    (cross_low_idx, cross_high_idx, cross_sub_sum) = max_cross_subarray(A, low, mid, high)
    
    # Checks for best solution and returns it
    if left_sub_sum >= right_sub_sum and left_sub_sum >= cross_sub_sum:
        return (left_low_idx, left_high_idx, left_sub_sum)
    elif right_sub_sum >= left_sub_sum and right_sub_sum >= cross_sub_sum:
        return (right_low_idx, right_high_idx, right_sub_sum)
    else:
        return (cross_low_idx, cross_high_idx, cross_sub_sum)
