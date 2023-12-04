import argparse
from dataclasses import dataclass
from collections import defaultdict
import math

def get_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return f.readlines()

class GRID:
    def __init__(self, raw_list):
        self.grid_rep = []

        self.max_x = len(raw_list[0]) - 1
        self.max_y = len(raw_list)
        for row in raw_list:
            vals = [val for val in row if val != '\n']
            self.grid_rep.append(vals)
        self.gear_map = defaultdict(list)

    def get_value(self, x, y):
        if x >= self.max_x or y >= self.max_y or x<0 or y<0:
            return None
        return self.grid_rep[y][x]
        

    def __str__(self):
        y_ls = []
        for y in range(self.max_y):
            x_ls = ''.join([self.get_value(x=x, y=y) for x in range(self.max_x)])
            y_ls.append(x_ls)
        return '\n'.join(y_ls)
            

class Number:
    def __init__(self, value, start_x, end_x, start_y, end_y):
        self.value = value
        self.value_int = int(value)
        self.start_x =start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        
    def __str__(self):
        return f'Value: {self.value}@ ({self.start_x}, {self.start_y}) -> ({self.end_x}, {self.end_y})'
    
    def has_neighboring_symbol(self, grid):
        @dataclass
        class numpos:
            x: int
            y: int
            val: str
            empty_left:bool
            empty_right: bool
        
        # Step 1 get all the numbers positions
        pos_list = []
        for i, v in enumerate(str(self.value), start=0):
            pos_list.append(numpos(x=i+self.start_x, y=self.start_y, val=str(v), empty_left=i==0, empty_right=i==len(self.value)-1))

        for pos in pos_list:
            # print(pos.val)
            vals = []
            # Is there something to the left?
            l_val = grid.get_value(pos.x-1, pos.y)
            l_bool = pos.empty_left and l_val and l_val != '.'
            if l_val == '*':
                grid.gear_map[(pos.x-1, pos.y)].append(self)
            #print(f'left: {l_val}, {l_bool}')

            # Is there something to the right?
            r_val = grid.get_value(pos.x+1, pos.y)
            r_bool = pos.empty_right and r_val and r_val != '.'
            if r_val == '*':
                grid.gear_map[(pos.x+1, pos.y)].append(self)

            # Is there something above?
            # print(f'above loc: {pos.x}, {pos.y-1}')
            a_val = grid.get_value(pos.x, pos.y-1)
            a_bool = a_val and a_val != '.'
            if a_val == '*':
                grid.gear_map[(pos.x, pos.y-1)].append(self)
            # print(f'above: {a_val}, {a_bool}')

            # Is there something below?
            # print(f'below {pos.x}, {pos.y+1} {grid.max_y}')
            b_val = grid.get_value(pos.x, pos.y+1)
            b_bool = b_val and b_val != '.'
            if b_val == '*':
                grid.gear_map[(pos.x, pos.y+1)].append(self)
            # print(f'below: {b_val}, {b_bool}')

            lu_val = grid.get_value(pos.x-1, pos.y-1)
            lu_bool = lu_val and lu_val != '.'
            if lu_val == '*':
                grid.gear_map[(pos.x-1, pos.y-1)].append(self)
            ld_val = grid.get_value(pos.x-1, pos.y+1)
            ld_bool = ld_val and ld_val != '.'
            if ld_val == '*':
                grid.gear_map[(pos.x-1, pos.y+1)].append(self)
            ru_val = grid.get_value(pos.x+1, pos.y-1)
            ru_bool = ru_val and ru_val != '.'
            if ru_val == '*':
                grid.gear_map[(pos.x+1, pos.y-1)].append(self)
            rd_val = grid.get_value(pos.x+1, pos.y+1)
            rd_bool = rd_val and rd_val != '.'
            if rd_val == '*':
                grid.gear_map[(pos.x+1, pos.y+1)].append(self)
            if any([l_bool, r_bool, a_bool, b_bool, lu_bool, ld_bool, ru_bool, rd_bool]):
                return True
        return False
        
def get_numbers(raw_input) -> list[Number]:
    nums = []
    for y, ls_y in enumerate(raw_input, start=0):
        num = ''
        start_x = None
        end_x = None
        for x, x_val in enumerate(ls_y, start=0):
            if x_val.isnumeric():
                # print(f'{x_val} = {x}, {y}')
                num += x_val
                if start_x == None:
                    start_x = x
                end_x = x
            else:
                if num:
                    nums.append(Number(num, start_x=start_x, end_x=end_x, start_y=y, end_y=y))
                start_x = None
                end_x = None
                num = ''
        if num:
            nums.append(Number(num, start_x=start_x, end_x=end_x, start_y=y, end_y=y))
        start_x = None
        end_x = None
        num = ''

    return nums
                    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Relative path to input file.", type=str)
    args = parser.parse_args()
    raw_input = get_input(args.input)
    grid = GRID(raw_input)
    numbers = get_numbers(raw_input=raw_input)
    print(grid)
    print(sum([num.value_int if num.has_neighboring_symbol(grid) else 0 for num in numbers]))
    total = 0
    print(grid.gear_map)
    print('aaa')
    for k, v in grid.gear_map.items():
        if len(v) >= 2:
            total += math.prod([x.value_int for x in v])
    print(total)
    # for num in numbers:
    #     print(num)
    #     print(num.has_neighboring_symbol(grid))