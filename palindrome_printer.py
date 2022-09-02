# code to print the even palindromes till n number


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def palindrome_printer(n):
    palindrome_list = []
    for i in range(0,n+1):
        if i % 2 == 0:
            if is_palindrome(i):
                palindrome_list.append(i)
    print(palindrome_list)


if __name__ == '__main__':
    number1 = 50
    palindrome_printer(number1)
    number2 = 100
    palindrome_printer(number2)