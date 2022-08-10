def searchRange(nums, target):
    res = [-1, -1]
    if not nums or not target in nums:
        return res    
    res[0] = nums.index(target)
    res[1] = len(nums) - nums[::-1].index(target) - 1
    return res
print(searchRange([], 9))

