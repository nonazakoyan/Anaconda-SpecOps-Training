def sumOfUnique(nums):
    sum = 0

    for i in nums:
        if nums.count(i) == 1:
            sum += i      
    return sum
