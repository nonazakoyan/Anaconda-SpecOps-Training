def my_func(lst):
    my_dict = {}
    for i in lst:
        my_dict[i] = lst.count(i)
    return my_dict

def findShortestSubArray(nums):
    dic = my_func(nums)
    arr = []
    new_arr = []
    for key in dic:
        if dic[key] == max(dic.values()):
            arr.append(key)
    if len(arr) == len(nums):
        return 1
    elif len(arr) == 1:
        return len(nums) - nums[::-1].index(arr[0]) - nums.index(arr[0])
    else:
        for i in range(len(arr)):
            idx1v = len(nums) - nums[::-1].index(arr[i]) - 1
            idx10 = nums.index(arr[i])
            new_arr.append(idx1v - idx10 + 1)
        return min(new_arr)
