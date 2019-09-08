def select_majority_element(A):
    '''
    Divide-and-conquer algorithm to find the majority element in a list A
    Running time is O(log(n)*n), instead of the naive brute force method O(n^2)
    '''
    # Handles the case when the bottom call in the recursion is an element of size 1
    if len(A) == 1:
        return A[0]
    # Check for equality when bottom recursion has a size of 2
    if len(A) ==  2:
        if A[0] == A[1]:
            return A[0]
        else:
            return A
        
    # Split into two halves (Divide-step)
    mid = int(len(A)/2)
    A_left = A[:mid]
    A_right = A[mid:]   
    
    left_major = select_majority_element(A_left)
    left_count = 0
    for element in A:
        if element == left_major:
            left_count += 1
        if left_count >= int(len(A)/2 + 1):
            return left_major
        
    # Find majority element in second half and check every other element in A O(n)
    right_major = select_majority_element(A_right)
    right_count = 0
    for element in A:
        if element == right_major:
            right_count += 1
        if right_count >= int(len(A)/2+1):
            return right_major
    
    return 'No majority element'
