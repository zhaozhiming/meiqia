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
