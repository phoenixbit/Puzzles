# this code is designed to print out the number of consonants in each word in a string


def consonant_counter(array):
    word_list = array.split()
    for i in range(len(word_list)):
        consonant_number = 0
        word_list_separated = word_list[i].split()
        for j in range(len(word_list_separated)):
            character_list = [*word_list_separated[j]]
            for k in range(len(character_list)):
                if character_list[k] != 'A' and character_list[k] != 'E' and character_list[k] != 'I' and character_list[k] != 'O' and character_list[k] != 'U' and character_list[k] != 'a' and character_list[k] != 'e' and character_list[k] != 'i' and character_list[k] != 'o' and character_list[k] != 'u':
                    consonant_number += 1
        print("The number of consonants in word " + str(i+1) + " is : " + str(consonant_number))


if __name__ == '__main__':
    sentence = "this is our time"
    consonant_counter(sentence)