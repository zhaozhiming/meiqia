import sys


def tee(file_name):
    output = open(file_name, 'w')

    for line in sys.stdin:
        output.write(line)

    output.close()


if __name__ == '__main__':
    tee(sys.argv[1])
