# code to find n numbers fibonacci series


def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_print(terms):
    for i in range(terms):
        print(fibonacci(i))


if __name__ == '__main__':
    num1 = 12
    fibonacci_print(num1)

