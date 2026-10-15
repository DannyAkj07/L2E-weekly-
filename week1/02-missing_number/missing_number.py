def find_missing(nums):
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] != 1:
            return nums[i] - 1


# def find_missing(nums,step=1) -> int:
#     first = nums[0]
#     last = nums[-1]

#     count = (last - first) + 1
#     expected_sum = count * (first + last) // 2
#     actual_sum = sum(nums)

#     result = expected_sum - actual_sum
#     return result


# print(find_missing([1, 2, 3, 5, 6]))
# print(find_missing([1, 3]))
print(find_missing([-2, -1, 1, 2]))
# print(find_missing([53, 52, 51, 50, 48]))
# print(find_missing([5, 6, 8, 9]))
