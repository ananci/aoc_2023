import re

total = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        ints = (re.findall(r'(\d)', line))
        if len(ints) < 2:
            val = int(ints[0]) * 11
        else:
            val = int(ints[0]) * 10 + int(ints[-1])
        print(val)
        total += val
print(total)