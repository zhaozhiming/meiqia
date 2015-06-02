# -*- coding: utf-8 -*-

# RLE压缩 RLE(Run Length Encoding),即行程压缩算法,是一个针对无损压缩的非常简单的算法。它用重复 字节和重复的次数来简单描述、
# 代替连续出现的重复字节。尽管简单并且对于通常的压缩非常低效,但 是由于非常适合有大量重复色块的图形,而且解压缩效率很高,
# 因此应用较为广泛。 RLE 可以使用很 多不同的方法,最简单的做法是:对于不重复内容,不做转换,对于重复内容,
# 用“控制字节+重复次 数+重复字节”三个字节表达。 请写出这种简单RLE压缩实现的代码。 当然,不能使用任何有直接帮助的第三方库。
# 请给出测试数据和输出结果。

def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
                # print lst
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q

# Method call
encode("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")
decode([('a', 5), ('h', 6), ('m', 7), ('u', 1), ('i', 7), ('a', 6)])
