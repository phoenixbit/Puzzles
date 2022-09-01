# this code is designed to flip the case of the whole string and if the character is a vowel we go two letters in front


def case_flipper_and_vowel_changer(word):
    word = word.swapcase().translate({ord('a'): ord('c'), ord('e'): ord('g'), ord('i'): ord('j'), ord('o'): ord('q'), ord('u'): ord('x'), ord('A'): ord('C'), ord('E'): ord('G'), ord('I'): ord('J'), ord('O'): ord('Q'), ord('U'): ord('X'), ord(' '): ord(' ')})
    print(word)


if __name__ == '__main__':
    word1 = "Python"
    case_flipper_and_vowel_changer(word1)
    word2 = "Hello, world!"
    case_flipper_and_vowel_changer(word2)