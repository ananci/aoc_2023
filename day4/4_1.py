import argparse
import math

def get_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return f.readlines()

def do_the_thing(raw_input) -> int:
    total_score = 0
    for line in raw_input:
        winning_raw, actual_raw = line.split(':')[1].split('|')
        winning_raw, actual_raw = winning_raw.strip(), actual_raw.strip()
        
        winning_list = [int(x) for x in winning_raw.split(' ') if x != '']
        actual_list = [int(x) for x in actual_raw.split(' ') if x != '' ]
        count = len([v for v in actual_list if v in winning_list])
        
        total_score += math.pow(2, count-1) if count > 0 else 0
    return total_score

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Relative path to input file.", type=str)
    args = parser.parse_args()
    raw_input = get_input(args.input)
    print(do_the_thing(raw_input=raw_input))