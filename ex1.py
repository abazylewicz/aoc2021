import queue

input = []
with open('ex1.input') as my_file:
    for line in my_file:
        input.append(int(line))

measurements = queue.Queue(3)
counter = 0
last = None
for i in input:
    if measurements.qsize() == 3:
        last = measurements.get()
    if last is not None and i > last:
        counter += 1
    measurements.put(i)

print(input)
print(counter)