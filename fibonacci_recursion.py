# code to find n numbers fibonacci series


def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_print(terms):
    fibonacci_array = []
    for i in range(terms):
        fibonacci_array.append(fibonacci(i))
    print(fibonacci_array)


if __name__ == '__main__':
    num1 = 12
    fibonacci_print(num1)

