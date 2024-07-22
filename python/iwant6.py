
def maxProductSubarray(nums, k):
    """
    Given an array of integers nums and an integer k, find the maximum possible product of any contiguous subarray of nums of length at most k.

    The product of an empty subarray is considered to be 1.

    Args:
        nums (list[int]): The input array of integers.
        k (int): The maximum length of the contiguous subarray.

    Returns:
        int: The maximum possible product of any contiguous subarray of nums of length at most k.
    """
    n = len(nums)
    max_product = float('-inf')

    for i in range(n):
        current_product = 1
        for j in range(i, min(i + k, n)):
            current_product *= nums[j]
            max_product = max(max_product, current_product)

    if max_product == float('-inf'):
      
       return max_product

nums3 = [1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]
k3 = 4
print(maxProductSubarray(nums3,k3))
