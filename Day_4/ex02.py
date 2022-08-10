def intersection(nums1, nums2):
    nums3 = []
    for i in set(nums1):
        for j in set(nums2):
            if i == j:
                nums3.append(i)
    return nums3
