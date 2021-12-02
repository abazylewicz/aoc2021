from dataclasses import dataclass


@dataclass
class Position:
    distance: int
    aim: int
    depth: int

    def move(self, move_value: int):
        self.distance += move_value
        self.depth += self.aim * move_value


pos = Position(0, 0, 0)
oldMeasurement = None
with open('ex2.input') as inputFile:
    for line in inputFile:
        direction, value = line.strip().split(' ')
        value: int = int(value)
        if direction == 'down':
            pos.aim += value
        elif direction == 'up':
            pos.aim -= value
        elif direction == 'forward':
            pos.move(value)
        else:
            raise RuntimeError(f"Unexpected direction {direction}")

print(pos.distance * pos.depth)
