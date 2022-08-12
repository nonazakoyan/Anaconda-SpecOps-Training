def bubble_sort(arr):
    for i in range(len(arr)):
        flag = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if flag == False:
            break
    return arr


# print(bubble_sort([46, 6, 9, 25, 1, 0]))