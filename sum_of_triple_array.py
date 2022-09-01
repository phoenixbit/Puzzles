# this code is desgined to find out if an array of three elements in another array has a sum value of zero


def sum_triple_array(array):
    place_holder_array = []
    for i in range(len(array)):
        sum_val = 0
        for j in range(3):
            sum_val += array[i][j]
        if sum_val == 0:
            place_holder_array.append("True")
        else:
            place_holder_array.append("False")

    print(place_holder_array)


if __name__ == '__main__':
    array1 = [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]
    sum_triple_array(array1)