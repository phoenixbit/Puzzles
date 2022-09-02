# code to print out the minimum even integer along with its index location


def minimum_even(array):
    minimum_value = -1
    minimum_list = []
    index_location = -1
    for i in range(len(array)):
        if array[i] % 2 == 0:
            if minimum_value == -1:
                minimum_value = array[i]
                index_location = i
            elif minimum_value > array[i]:
                minimum_value = array[i]
                index_location = i
    if minimum_value == -1:
        print(minimum_list)
    else:
        minimum_list.append(minimum_value)
        minimum_list.append(index_location)
        print(minimum_list)


if __name__ == '__main__':
    array1 = [1, 9, 4, 6, 10, 11, 14, 8]
    minimum_even(array1)
    array2 = [1, 7, 4, 4, 9, 2]
    minimum_even(array2)
