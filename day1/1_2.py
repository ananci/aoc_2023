import re
val_dict = {'one': '1', 'two':'2', 'three':'3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
total = 0

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