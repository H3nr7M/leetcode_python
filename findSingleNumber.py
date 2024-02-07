def find_single_number(nums):
    bit_vector = [0] * 32
    for num in nums:
        for i in range(32):
            if (num & (1 << i)) != 0:
                bit_vector[i] += 1
    result = 0
    for i, count in enumerate(bit_vector):
        if count % 3 != 0:
            result |= 1 << i
    return result

print(find_single_number([6, 1, 3, 3, 3, 6, 6]))