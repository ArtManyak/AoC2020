from common.common import get_lines


def count_adjust_occupied(grid, i, j):
    result = 0
    dxs = dys = [-1, 0, 1]
    for dx in dxs:
        for dy in dys:
            if dx == 0 and dy == 0:
                continue
            if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0]):
                result += grid[i + dx][j + dy] == '#'
    return result


def count_adjust_occupied_2(grid, i, j):
    result = 0
    dxs = dys = [-1, 0, 1]
    for dx in dxs:
        for dy in dys:
            mult = 1
            if dx == dy == 0:
                continue
            while 0 <= i + mult * dx < len(grid) and 0 <= j + mult * dy < len(grid[0]):
                if grid[i + mult * dx][j + mult * dy] == 'L':
                    break
                if grid[i + mult * dx][j + mult * dy] == '#':
                    result += 1
                    break
                mult += 1
    return result


def simulate_life(grid, count_occupied, allow_occupied):
    new_grid = grid.copy()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L' and count_occupied(grid, i, j) == 0:
                new_grid[i] = ''.join((new_grid[i][:j], '#', new_grid[i][j + 1:]))
            if grid[i][j] == '#' and count_occupied(grid, i, j) >= allow_occupied:
                new_grid[i] = ''.join((new_grid[i][:j], 'L', new_grid[i][j + 1:]))
    return new_grid


def solve(grid, count_occupied, allow_occupied):
    while (new_grid := simulate_life(grid, count_occupied, allow_occupied)) != grid:
        grid = new_grid
    return sum(i.count('#') for i in new_grid)


if __name__ == '__main__':
    data = [x.strip() for x in get_lines("in.txt")]
    print(solve(data, count_adjust_occupied, 4))
    print(solve(data, count_adjust_occupied_2, 5))
