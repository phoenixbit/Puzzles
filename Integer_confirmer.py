# in this puzzle program we have to check to find for exactly 2 occurrences of 19 and at least 3 occurrences of 5


def occurrence_checker(array):
    flag_nt = 0
    flag_f = 0

    for i in range(len(array)):
        if array[i] == 19:
            flag_nt += 1
        elif array[i] == 5:
            flag_f += 1
        else:
            continue

    if flag_nt == 2 and flag_f >= 3:
        print("True")
        return
    else:
        print("False")
        return


if __name__ == '__main__':
    occ_array1 = [1, 2, 3, 4, 5, 19, 19, 5, 4, 5]
    occurrence_checker(occ_array1)
    occ_array2 = [1, 2, 3, 4, 5, 19, 19, 5, 4]
    occurrence_checker(occ_array2)
    occ_array3 = [1, 2, 5, 5, 4, 5, 19, 19, 5, 4]
    occurrence_checker(occ_array3)
    occ_array4 = [1, 2, 5, 4, 5, 19, 5, 4]
    occurrence_checker(occ_array4)