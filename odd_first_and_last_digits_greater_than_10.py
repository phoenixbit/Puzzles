# code is to print out the array of numbers greater than 10 with first and last digits being odd


def odd_first_and_last(array):
    resultant_array = []
    for i in range(len(array)):
        if array[i] > 10:
            digit = array[i] % 10
            if digit % 2 != 0:
                digit_value = array[i] // 10
                while digit_value != 0:
                    if digit_value > 9:
                        digit_value = digit_value // 10
                    else:
                        if digit_value % 2 != 0:
                            resultant_array.append(array[i])
                        digit_value = digit_value // 10

    print(resultant_array)


if __name__ == '__main__':
    array1 = [1, 3, 79, 10, 4, 1, 39, 62]
    odd_first_and_last(array1)

