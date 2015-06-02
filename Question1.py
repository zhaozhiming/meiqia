# Give me a function that takes a list of numbers and returns only the even ones, divided by two.
# (please use list comprehension)


def evens(array):
    return [num for num in array if num % 2 == 0]


if __name__ == '__main__':
    print evens([1, 2, 3, 4, 5])
