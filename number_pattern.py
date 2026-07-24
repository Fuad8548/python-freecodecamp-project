def number_pattern(n):
    nums = []
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        for num in range(1, n + 1):
            nums.append(str(num))
            joined_nums = ' '.join(nums)
        return joined_nums

n = 4
print(number_pattern(n))