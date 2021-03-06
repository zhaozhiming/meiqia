# -*- coding: utf-8 -*-

# 用python写一个程序，找出数组中差值为K的数共有几对
#
# 示例：
# 差值k=4 and 数组是[7, 6, 23,19,10,11, 9, 3, 15]
# 这样的结果是(7,11) (7,3) (6,10) (19,23) (15,19) (15,11) 共6对
#
# 从标准输入读入两行数据
# 5 2
# 1 5 3 4 2
#
# 第一行代表N和K, N是数组是一共有多少数字，K是所要求的差值
# 第二是数组，空白分格
#
# 输出到标准输出
#
#
# Sample Input #00:
# 5 2
# 1 5 3 4 2
# Sample Output #00:
# 3
# Sample Input #01:
# 10 1
# 363374326 364147530 61825163 1073065718 1281246024 1399469912 428047635 491595254 879792181 1069262793
# Sample Output #01:
# 0

def calc():
    first = raw_input('Sample Input #00: \n')
    second = raw_input('')

    n, k = [int(x) for x in first.split()]
    array = [int(x) for x in second.split()]

    result = []
    for i in range(0, n):
        for j in range(i + 1, n):
            if abs(array[i] - array[j]) == k:
                result.append(str(array[i]) + str(array[j]))

    print 'Sample Input #01:'
    print len(result)


if __name__ == '__main__':
    calc()
