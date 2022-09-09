# code to check if the given files are of the right format or not and to check if they are valid files at all


file_extension_map = {".jpg": 1, ".png": 2, ".txt": 3, ".exe": 4, ".dll": 5}


def file_checker(array):
    return_array = []
    for i in range(len(array)):
        file = array[i]
        last_four_char = file[-4:]
        if file_extension_map.__contains__(last_four_char):
            period_counter = 0
            number_counter = 0
            character_list = [*file]
            for k in range(len(character_list)):
                character = character_list[k]
                if character == '.':
                    period_counter += 1
                elif character.isnumeric():
                    number_counter += 1
            if period_counter >= 2 or number_counter >= 4:
                return_array.append("False")
            else:
                return_array.append("True")
        else:
            return_array.append("False")
    print(return_array)


if __name__ == '__main__':
    array1 = ['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
    file_checker(array1)
