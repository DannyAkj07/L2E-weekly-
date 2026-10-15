def remove_duplicates(nums):
    new_nums = []
    for item in nums:
        if not nums:
            return []
        if item not in new_nums:
            new_nums.append(item)
    return new_nums

print(remove_duplicates([]))