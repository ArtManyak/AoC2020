from common.common import get_lines


def solve(xd: int, yd: int) -> int:
    cur_x, cur_y = 0, 0
    result = 0
    while cur_y <= len(grid) - 1:
        result += 1 if grid[cur_y][cur_x] == '#' else 0
        cur_x = (cur_x + xd) % (len(grid[cur_y]) - 1)
        cur_y += yd
    return result


grid = get_lines('in.txt')
if __name__ == '__main__':
    print(solve(3, 1))
    print(solve(1, 1) * solve(3, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2))
