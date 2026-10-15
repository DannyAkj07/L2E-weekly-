def rotate_list(nums, k):
    new_num = []
    if not nums:
        return []
    if k == len(nums) or k == 0:
        return nums
    if k > len(nums):
        k = k % len(nums)
    new_num = nums[-k:] + nums[:-k]
    return new_num

print(rotate_list([1, 2, 3, 4, 5], k=7))
