def findMaxConsecutiveOnes(nums):
    counter = 0
    max = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            if counter > max:
                max = counter
            counter = 0
        elif i == len(nums) -1:
            counter +=1
            if counter > max:
                max = counter
            counter = 0
        else:
            counter += 1
    return max
