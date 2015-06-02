# -*- coding: utf-8 -*-
# 一个数组，里面都是整数，请编写一个程序，使用快速排序排序，并打印排序后的结果，请给出测试集和输出结果。

# 1．先从数列中取出一个数作为基准数。
# 2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
# 3．再对左右区间重复第二步，直到各区间只有一个数。

def sub_sort(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array, low, high):
    if low < high:
        key_index = sub_sort(array, low, high)
        quick_sort(array, low, key_index)
        quick_sort(array, key_index + 1, high)


if __name__ == '__main__':
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print array
    quick_sort(array, 0, len(array) - 1)
    print array
