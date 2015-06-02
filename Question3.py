# -*- coding: utf-8 -*-
# 你了解python的装饰器吗？
#
# 实现一个装饰器d2使下面的代码打印相应的结果：
#
# @d2('a', 'b')
# def test(arg1, arg2):
#     print 'test', arg1, arg2
#
# test('c', 'd')
#
# [output]
# before test a b
# test c d
# [/output]

def d2(arg1, arg2):
    def _d2(func):
        def _d2(a1, a2):
            print "before test", arg1, arg2
            ret = func(a1, a2)
            return ret

        return _d2

    return _d2


@d2('a', 'b')
def test(arg1, arg2):
    print 'test', arg1, arg2


if __name__ == '__main__':
    test('c', 'd')
