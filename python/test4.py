def max_contiguous_subarrays(nums, k):
    cumulative_sum_freq = {0: 1}
    max_subarrays = 0
    cum_sum = 1

    for num in nums:
        cum_sum = (cum_sum + num) % k
        if cum_sum < 0:
            cum_sum += k
        if cum_sum in cumulative_sum_freq:
            max_subarrays = (max_subarrays + cumulative_sum_freq[cum_sum]) % (10**9 + 7)
        cumulative_sum_freq[cum_sum] = cumulative_sum_freq.get(cum_sum, 0) + 1

    return max_subarrays

# Test the combined function with the provided example
output = max_contiguous_subarrays([1, 2, 3, 4, 5], 3)
print(output)  # Expected output should be 4
