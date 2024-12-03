import copy

safe_levels = 0

def test_safe(line):
    counter = 0
    increasing = int(line[0]) < int(line[1])
    safe = True

    while counter < len(line) - 1:
        diff = abs(int(line[counter]) - int(line[counter + 1]))
        increase_or_decrease = int(line[counter]) < int(line[counter + 1])
        if increase_or_decrease == increasing and diff >= 1 and diff <= 3:
            counter += 1
        else:
            return counter
    return -1

with open("input.txt", "r") as input_file:
    for line in input_file:
        line = line.split()
        output = test_safe(line)

        if output == -1:
            # The line is already safe
            safe_levels += 1
        else:
            # Test all possible single removals
            is_safe = False
            for i in range(len(line)):
                modified_line = copy.deepcopy(line)
                modified_line.pop(i)
                if test_safe(modified_line) == -1:
                    is_safe = True
                    break
            
            if is_safe:
                safe_levels += 1

print(safe_levels)
