distance = 0
aim = 0
depth = 0
oldMeasurement = None
with open('ex2.input') as inputFile:
    for line in inputFile:
        direction, value = line.strip().split(' ')
        value = int(value)
        if direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
        elif direction == 'forward':
            distance += value
            depth += aim * value
        else:
            raise RuntimeError(f"Unexpected direction {direction}")


print(distance * depth)
