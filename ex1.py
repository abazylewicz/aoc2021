import queue

measurements = queue.Queue(3)
counter = 0
oldMeasurement = None
with open('ex1.input') as my_file:
    for line in my_file:
        newMeasurement = int(line)
        if measurements.full():
            oldMeasurement = measurements.get()
        if oldMeasurement is not None and newMeasurement > oldMeasurement:
            counter += 1
        measurements.put(newMeasurement)

print(counter)
