import re
val_dict = {'one': '1', 'two':'2', 'three':'3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
total = 0

def get_ints(line:str) -> list[int]:
    regex_group_str = '|'.join(val_dict.keys())
    regex_group_str = f'(?=({regex_group_str}|\d))'
    found = re.findall(regex_group_str, line)
    return_list = []
    for f in found:
        val = val_dict.get(f, f)
        return_list.append(int(val))
    return return_list

def get_first_last_new_number(ints: list[int]) -> int:
    if len(ints)<2:
        val = ints[0]*11
    else:
        val = ints[0]*10 + ints[-1]
    return val

def get_sum_from_list(lines:list[str]) -> int:
    total = 0
    for line in lines:
        ints = get_ints(line)
        val = get_first_last_new_number(ints)
        total += val
    return total


with open('input.txt', 'r') as f:
    lines = f.readlines()
    print(f'From input: {get_sum_from_list(lines)}')


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
print(f'From test input: {get_sum_from_list(test_list)}')