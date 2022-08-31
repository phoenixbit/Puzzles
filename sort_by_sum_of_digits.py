# code to sort the given array by the sum of their digits


def sort_sum_array(nums):
    return sorted(nums, key=lambda n: sum(int(c) for c in str(n) if c != "-"))


if __name__ == '__main__':
    array1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(sort_sum_array(array1))