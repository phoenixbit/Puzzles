# code to remove the duplicates in an array along with the preservation of the order of the original array


def duplicate_remover(array):
    duplicate_map = {}
    resultant_array = []
    for i in range(len(array)):
        if duplicate_map.__contains__(array[i]):
            continue
        else:
            duplicate_map[i] = array[i]
            resultant_array.append(array[i])
    print(resultant_array)


if __name__ == '__main__':
    array1 = [1, 3, 4, 10, 4, 1, 43]
    duplicate_remover(array1)


