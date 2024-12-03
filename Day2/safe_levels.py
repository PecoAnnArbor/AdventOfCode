line = []
safe_levels = 0

with open("input.txt", "r") as input_file:
    for line in input_file:
        line = line.split()
        print(line)

        increasing = int(line[0]) < int(line[1])
        print(increasing)
        counter = 0
        safe = True

        while counter < len(line) - 1:
            print(counter)
            diff = abs(int(line[counter]) - int(line[counter + 1]))
            i = int(line[counter]) < int(line[counter + 1])
            if i == increasing and diff >= 1 and diff <= 3:
                counter += 1
            else:
                safe = False
                break

        if safe:
            safe_levels += 1


print(safe_levels)

            



