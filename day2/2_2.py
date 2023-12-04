import argparse
import re


def get_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return f.readlines()


class Game:
    def __init__(self, id:int, moves = list[dict[str:int]]):
        self.id = id
        self.moves = moves

    def __str__(self):
        return f'ID:{self.id} moves:{self.moves}'

    def _get_max_per_color(self, color_str):
        return max([move.get(color_str, 0) for move in self.moves])

    def is_possible(self, p_bag: dict[str: int]) -> bool:
        return all([self._get_max_per_color(p_color) <= p_count for (p_color, p_count) in p_bag.items()])
              
    def get_power_min_blocks(self) -> int:
        max_red = self._get_max_per_color('red') or 1
        max_blue = self._get_max_per_color('blue') or 1
        max_green = self._get_max_per_color('green') or 1
        return max_red * max_blue * max_green




proposed_bag = {'red': 12, 'green': 13, 'blue': 14}

def parse_line(line) -> Game:
    moves = []
    id_str, raw_moves = line.split(':', 1)
    id = int(id_str.split(' ')[1])
    split_moves = raw_moves.split(';')
    for split_move in split_moves:
        blocks = {}
        blocks = {color: int(count) for (count, color) in re.findall(r' *([\d]+) ([a-z]+)', split_move)}
        moves.append(blocks)
    return Game(id, moves)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Relative path to input file.", type=str)
    args = parser.parse_args()
    games = [parse_line(line) for line in get_input(args.input)]
    print(proposed_bag)
    print(sum([x.id if x.is_possible(p_bag=proposed_bag) else 0 for x in games]))
    print(sum([x.get_power_min_blocks() for x in games]))
    print('END')