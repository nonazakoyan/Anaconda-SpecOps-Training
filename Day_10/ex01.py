def removeDuplicates(nums):
    k = 1
    expectedNums = [nums[0]]
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            expectedNums.append(nums[i + 1])
            k += 1
    nums = expectedNums
    return k

