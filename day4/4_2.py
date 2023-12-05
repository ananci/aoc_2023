import argparse
import math

def get_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return f.readlines()

class Card:
    def __init__(self, line):
        winning_raw, actual_raw = line.split(':')[1].split('|')
        winning_raw, actual_raw = winning_raw.strip(), actual_raw.strip()
        
        winning_list = [int(x) for x in winning_raw.split(' ') if x != '']
        actual_list = [int(x) for x in actual_raw.split(' ') if x != '' ]
        count = len([v for v in actual_list if v in winning_list])
        self.winning_count = count if count > 0 else 0
        self.copy_count = 1

def do_the_thing(raw_input) -> int:
    card_list = [Card(line) for line in raw_input]
    for i, card in enumerate(card_list, start=0):
        print(f'Winning Count: {card.winning_count}')
        for x in range(card.winning_count):
            index = i + x + 1
            print(index)
            if index > len(card_list) - 1 :
                continue
            card_list[index].copy_count += card.copy_count

    return sum([c.copy_count for c in card_list])
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Relative path to input file.", type=str)
    args = parser.parse_args()
    raw_input = get_input(args.input)
    print(do_the_thing(raw_input=raw_input))