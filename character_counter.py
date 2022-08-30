# code to print out the array with the lesser number of characters


def character_counter(array1, array2):
    character_val1 = 0
    character_val2 = 0
    for i in range(len(array1)):
        character_val1 += len(array1[i])

    for j in range(len(array2)):
        character_val2 += len(array2[j])

    if character_val1 > character_val2:
        print(array1)

    else:
        print(array2)


if __name__ == '__main__':
    character_counter(['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider'])
