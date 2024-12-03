left, right = [], {}

with open("input.txt", "r") as input_file:
    for line in input_file:
        parts = line.split()
        left.append(int(parts[0]))
        if int(parts[1]) in right:
            right[int(parts[1])] += 1
        else:
            right[int(parts[1])] = 1


similarity_score = 0

for i in left:
    if i in right:
        similarity_score += i * right[i]

print(similarity_score)
            