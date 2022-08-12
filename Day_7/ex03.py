from traceback import print_tb


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                print('arr[j] -%d arr[j-1]' % arr[j], arr[j - 1])
                arr[j], arr[j - 1] = arr[j - 1], arr[j]      
    return arr

print(insertion_sort([7,46, 6, 9, 25, 1]))
