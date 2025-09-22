def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    return max(numbers)
    previous_num = 0
    for num in numbers:
        if num > previous_num:
            num = previous_num
    return num


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
