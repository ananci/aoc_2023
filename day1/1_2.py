import re

# Code Golfed solution in single list comprehension.
def get_sum2(ls: list[str]) -> int:
    return sum([int(y[0] + y[-1]) for v in [['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']] for l in ls for y in [[x if x not in v else str(v.index(x) + 1) for x in re.findall(f"(?=({'|'.join(v)}|\d))", l)]]])


# More readable solution.
def get_sum(lines: list[str]) -> int:
    total = 0
    val_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    regex_group_str = f"(?=({'|'.join(val_list)}|\d))"
    for line in lines:
        found = [x if x not in val_list else str(val_list.index(x) + 1) for x in re.findall(regex_group_str, line)]
        val = found[0] + found[-1]
        total += int(val)
    return total

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        print(f'From input: {get_sum(lines)}')
        print(f'From input: {get_sum2(lines)}')

    test_list = [
        # 'two1nine',
        # 'eightwothree',
        # 'abcone2threexyz',
        # 'xtwone3four',
        # '4nineeightseven2',
        # 'zoneight234',
        # '7pqrstsixteen',
        'eighthree',
        'sevenine'
    ]

    print(f'From test input: {get_sum(test_list)}')
    print(f'From test input: {get_sum2(test_list)}')