left, right = [], []

with open("input.txt", "r") as input_file:
    for line in input_file:
        parts = line.split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))

left.sort()
right.sort()

distance = 0

for i in range(len(left)):
    distance += abs(left[i] - right[i])

print(distance)
        
