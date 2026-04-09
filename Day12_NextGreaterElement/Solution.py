def next_greater_element(nums1, nums2):
    stack = []
    next_greater = {}

    for num in nums2:
        while stack and num > stack[-1]:
            prev = stack.pop()
            next_greater[prev] = num
        stack.append(num)

    # Remaining elements → no greater
    for num in stack:
        next_greater[num] = -1

    # Build result for nums1
    result = []
    for num in nums1:
        result.append(next_greater[num])

    return result


# Example run
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(next_greater_element(nums1, nums2))  # Output: [-1,3,-1]