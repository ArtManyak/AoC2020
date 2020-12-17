import copy

from common.common import get_lines


def count_adjust_occupied(grid, x, y, z, w):
    result = 0
    deltas = [-1, 0, 1]
    for dw in deltas:
        for dz in deltas:
            for dy in deltas:
                for dx in deltas:
                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                        continue
                    if -6 <= x + dx < len(grid[w][z][y]) - 6 and -6 <= y + dy < len(grid[w][z]) - 6 and -6 <= z + dz < 7 and -6 <= w + dw < 7:
                        result += grid[w + dw][z + dz][y + dy][x + dx] == '#'
    return result


def simulate_life(grid, count_occupied):
    new_grid = copy.deepcopy(grid)
    for w in grid:
        for z in grid[w]:
            for y in grid[w][z]:
                for x in grid[w][z][y]:
                    if grid[w][z][y][x] == '#':
                        if 2 <= count_occupied(grid, x, y, z, w) <= 3:
                            new_grid[w][z][y][x] = '#'
                        else:
                            new_grid[w][z][y][x] = '.'
                    else:
                        if count_occupied(grid, x, y, z, w) == 3:
                            new_grid[w][z][y][x] = '#'
                        else:
                            new_grid[w][z][y][x] = '.'
    return new_grid


if __name__ == '__main__':
    input_lines = [x.strip() for x in get_lines("in.txt")]
    data = dict()
    for w in range(-6, 7):
        data[w] = dict()
        for z in range(-6, 7):
            data[w].update({z: dict()})
            for y in range(-6, len(input_lines) + 6):
                data[w][z].update({y: dict()})
                for x in range(-6, len(input_lines) + 6):
                    data[w][z][y].update({x: '.'})
    for y, line in enumerate(input_lines):
        for x, cell in enumerate(line):
            data[0][0][y].update({x: cell})

    for _ in range(6):
        data = simulate_life(data, count_adjust_occupied)
    result = 0
    for w in data:
        for z in data[w]:
            for y in data[w][z]:
                for x in data[w][z][y]:
                    result += data[w][z][y][x] == '#'
    print(result)
