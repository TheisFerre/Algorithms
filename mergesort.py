def mergesort(l):
    """
    Function for mergesorting a list of elements
    """
    def merge(l1, l2):
        """
        Helper function to merge two sorted list
        """
        l1_idx = 0
        l2_idx = 0
        merged_list_idx = 0
        merged_list = [0] * (len(l1) + len(l2) )

        while l1_idx < len(l1) and l2_idx < len(l2):
            if l1[l1_idx] < l2[l2_idx]:
                merged_list[merged_list_idx] = l1[l1_idx]
                l1_idx += 1
                merged_list_idx += 1
            else:
                merged_list[merged_list_idx] = l2[l2_idx]
                l2_idx += 1
                merged_list_idx += 1

        if (l1_idx) < len(l1):
            for i in range(l1_idx, len(l1)):
                merged_list[merged_list_idx] = l1[l1_idx]
                merged_list_idx += 1
                l1_idx += 1

        elif (l2_idx) < len(l2):
            for i in range(l2_idx, len(l2)):
                merged_list[merged_list_idx] = l2[l2_idx]
                merged_list_idx += 1
                l2_idx += 1

        return merged_list
    
    # Base case when there is a single element in a list
    # By definition this will be sorted
    if len(l) <= 1:
        return l
    
    else:
        mid = int(len(l)/2)
        
        # Recurse on both halves
        left_half = split(l[0:mid])
        right_half = split(l[mid:])
        
        # Merge both halves at bottom of recursion
        return merge(left_half, right_half)
