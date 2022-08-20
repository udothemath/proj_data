from functools import partial


def multiply(a, b):
    return a * b


def use_partial(x, y=5):
    f = partial(multiply, y)
    result = f(x)
    print(result)


if __name__ == "__main__":
    print(multiply(a=3, b=5))
    use_partial(2)
    use_partial(10)

# Ref
# https://www.pythontutorial.net/python-basics/python-partial-functions/
# https://www.geeksforgeeks.org/partial-functions-python/
