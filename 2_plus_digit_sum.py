# code is designed to find the sum of the first k elements in an array which are greater than 2 digits


def two_digit_sum(array, k):
    sum_val = 0
    for i in range(k):
        if array[i] > 99 or array[i] < -99:
            sum_val += array[i]

    print(sum_val)


if __name__ == '__main__':
    array1 = [4, 5, 17, 9, 14, 108, -9, 12, 76]
    array2 = [114, 215, -117, 119, 14, 108, -9, 12, 76]
    two_digit_sum(array1, 5)
    two_digit_sum(array1, 6)
    two_digit_sum(array2, 6)
    two_digit_sum(array2, 5)
