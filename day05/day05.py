import math

from common.common import get_lines


def do_bin_search(row: str, lower: int, upper: int, lower_key: str) -> int:
    middle = lower
    for i in row:
        if i == lower_key:
            middle = upper = math.floor((lower + upper) / 2)
        else:
            middle = lower = math.ceil((lower + upper) / 2)
    return middle


def solve(row: str) -> int:
    final_row = do_bin_search(row[:7], 0, 127, 'F')
    final_place = do_bin_search(row[7:], 0, 7, 'L')
    return final_row * 8 + final_place


rows = get_lines('in.txt')
if __name__ == '__main__':
    s = set(map(solve, rows))
    print(next(i for i in range(min(s), max(s)) if i not in s))
