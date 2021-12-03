oldMeasurement = None
results = []
total = 0
init = True
with open('ex3.input') as inputFile:
    for line in inputFile:
        if init:
            results = [0] * len(line.strip())
            init = False
        for index in range(0, len(line)):
            if line[index] == '1':
                results[index] += 1
        total += 1


def most_common_bit(ones: int, threshold: int) -> int:
    if ones > threshold:
        return 1
    else:
        return 0


def negate(bit_string) -> list:
    return list(map(lambda x: abs(x - 1), bit_string))


gamma = list(map(lambda c: most_common_bit(c, total / 2), results))
epsilon = negate(gamma)

gamma_string = ''.join([str(bit) for bit in gamma])
epsilonString = ''.join([str(bit) for bit in epsilon])
gammaValue = int(gamma_string, 2)
print(gammaValue)
epsilonValue = int(epsilonString, 2)
print(epsilonValue)

print(gammaValue * epsilonValue)
