# code to print out piles given number of stone piles


def stone_pile(number):
    pile_array = []
    pile_val = number
    for i in range(number):
        pile_array.append(pile_val)
        pile_val += 2
    print(pile_array)


if __name__ == '__main__':
    stone_pile(4)
    stone_pile(5)
