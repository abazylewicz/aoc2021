lines = []
with open('ex3.input') as inputFile:
    for file_line in inputFile:
        lines.append(file_line)


def find_most_and_least_common_bit(input_lines):
    results = []
    total = 0
    init = True
    for line in input_lines:
        if init:
            results = [0] * len(line.strip())
            init = False
        for index in range(0, len(line)):
            if line[index] == '1':
                results[index] += 1
        total += 1
    mcb = list(map(lambda c: most_common_bit(c, total / 2), results))
    lcb = negate(mcb)
    return mcb, lcb


def most_common_bit(ones: int, threshold: int) -> int:
    if ones >= threshold:
        return 1
    else:
        return 0


def negate(bit_string) -> list:
    return list(map(lambda x: abs(x - 1), bit_string))


# part 2
def find_rating(most_common):
    input_left = lines

    for bit_index in range(0, len(input_left[0])):
        mcb, lcb = find_most_and_least_common_bit(input_left)
        if most_common:
            criteria = mcb
        else:
            criteria = lcb
        input_left = list(filter(lambda l: l[bit_index] == str(criteria[bit_index]), input_left))
        if (len(input_left)) == 1:
            return input_left[0]
    raise RuntimeError(f"should have not happened: {input_left}")


def binary_list_to_int(binary_list):
    binary_string = ''.join([str(bit) for bit in binary_list])
    return int(binary_string, 2)


oxygen_rating = binary_list_to_int(find_rating(True))
life_rating = binary_list_to_int(find_rating(False))
print(oxygen_rating)
print(life_rating)
print((oxygen_rating * life_rating))
