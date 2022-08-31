# code to find the product of the digits of a number which are odd in value

product_val = 0


def product_of_odd(number, product_val):
    digit = number % 10
    if digit % 2 != 0:
        if product_val == 0:
            product_val += digit
        else:
            product_val *= digit
    number = number // 10
    if number == 0:
        print(product_val)
        return
    product_of_odd(number, product_val)


if __name__ == '__main__':
    value1 = 123456789
    value2 = 2468
    product_of_odd(value1, product_val)
    product_of_odd(value2, product_val)
