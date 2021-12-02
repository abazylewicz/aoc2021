distance = 0
depth = 0
oldMeasurement = None
with open('ex2.input') as inputFile:
    for line in inputFile:
        direction, value = line.strip().split(' ')
        if direction == 'down':
            depth += int(value)
        elif direction == 'up':
            depth -= int(value)
        elif direction == 'forward':
            distance += int(value)
        else:
            raise RuntimeError(f"Unexpected direction {direction}")


print(distance * depth)
