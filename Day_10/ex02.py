def merge(nums1, nums2, n, m):
    i = 0
    j = 0
    if m == 0:
        nums1 = nums2
        return
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            i +=1
        else:
            nums1[i + 1:(m + 2)] = nums1[i:(m + 1)]
            nums1[i] = nums2[j]
            j += 1
    nums1[i + 1:] =nums2[j:] 
    print(nums1)
