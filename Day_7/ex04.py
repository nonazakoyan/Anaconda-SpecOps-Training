def ft_merge(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left)  and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i +=1
        else:
            res.append(right[j])
            j += 1
    if i < len(left):
        res.extend(left[i:])
    if j < len(right):
        res.extend(right[j:])
    return res


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return ft_merge(left, right)