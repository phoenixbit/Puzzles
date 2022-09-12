# code to apend an integer to the array to make the total sum of the array 0


def append_integer(array):
    sum_variable = 0
    appended_value = 0
    for i in range(len(array)):
        sum_variable += array[i]
    if sum_variable != 0:
        appended_value -= sum_variable
    print(appended_value)


if __name__ == '__main__':
    array1 = [1, 2, 3, 4, 5]
    append_integer(array1)
