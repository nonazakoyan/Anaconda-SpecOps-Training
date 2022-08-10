    # idx1v = len(nums) - nums[::-1].index(zangvac[0]) - 1
    # idx10 = nums.index(zangvac[0])

    # urish_zangvac.append(idx1v - idx10 + 1)
    # urish_zangvac.append(nums.index(zangvac[1]) - nums.index(zangvac[0]))
    # urish_zangvac.append(len(nums) - nums[::-1].index(zangvac[1]) - 1 - nums.index(zangvac[1]))
    # if len(nums) - nums[::-1].index(zangvac[0]) - 1 > nums.index(zangvac[1]):
    #     urish_zangvac.append(len(nums) - nums[::-1].index(zangvac[0])  - nums.index(zangvac[1]))
    # elif len(nums) - nums[::-1].index(zangvac[0]) - 1 < nums.index(zangvac[1]):
    #     urish_zangvac.append(nums.index(zangvac[1]) - (len(nums) - nums[::-1].index(zangvac[0]) - 1))
    # print(urish_zangvac)
    # print(len(nums) - nums[::-1].index(zangvac[1]) - 1)

def my_func(lst):
    my_dict = {}
    for i in lst:
        my_dict[i] = lst.count(i)
    return my_dict

def findShortestSubArray(nums):
    dic = my_func(nums)
    zangvac = []
    nor_zangvac = []
    for key in dic:
        if dic[key] == max(dic.values()):
            zangvac.append(key)
        
    print(zangvac)
    if len(zangvac) == len(nums):
        return len(nums)
    elif len(zangvac) == 1:
        return len(nums) - nums[::-1].index(zangvac[0]) - nums.index(zangvac[0])
    else:
        for i in range(len(zangvac)):
            idx1v = len(nums) - nums[::-1].index(zangvac[i]) - 1
            idx10 = nums.index(zangvac[i])
            nor_zangvac.append(idx1v - idx10 + 1)
            print(nor_zangvac)
        return min(nor_zangvac)
# print(findShortestSubArray([1,2,2,1,3,1,4,2]))

a = 3
b = a
a = a + 2
print(id(a), id(b))