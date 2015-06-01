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
