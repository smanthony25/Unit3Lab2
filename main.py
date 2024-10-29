# Sean A
# n factorial
# Use 3 different kinds of loops to make factiorials and show the differences


def for_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def while_factorial(n):
    factorial = 1
    while n >= 1:
        factorial *= n
        n -= 1
    return factorial


def recursion_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursion_factorial(n - 1)


def testNum(n):
    print(f"Testing {n}")
    forFac = for_factorial(n)
    print(f"For loop calculation: {forFac}")
    whileFac = while_factorial(n)
    print(f"While loop calculation: {whileFac}")
    try:
        recursionFac = recursion_factorial(n)
        print(f"Recursion loop calculation: {recursionFac}")
    except:
        print("Recursion failed!")
    print("\n")


def main():
    n = 4
    testNum(n)
    n = 1000
    testNum(n)


if __name__ == '__main__':
    main()
