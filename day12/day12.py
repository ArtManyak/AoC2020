import math

from common.common import get_lines


def rotate(current_direction, angle):
    (x, y) = current_direction
    angle = math.radians(angle)
    cs, sn = int(math.cos(angle)), int(math.sin(angle))
    return x * cs - y * sn, x * sn + y * cs


def make_step(current_position, current_direction, action, count):
    (x, y), (dx, dy) = current_position, current_direction
    if action == 'N':
        return current_position, (dx, dy + count)
    if action == 'S':
        return current_position, (dx, dy - count)
    if action == 'E':
        return current_position, (dx + count, dy)
    if action == 'W':
        return current_position, (dx - count, dy)
    if action == 'L':
        return current_position, rotate(current_direction, count)
    if action == 'R':
        return current_position, rotate(current_direction, -count)
    if action == 'F':
        return (x + dx * count, y + dy * count), current_direction


def solve(start_position, start_direction, route):
    current_position, current_direction = start_position, start_direction
    for step in route:
        action, count = step[0], int(step[1:])
        current_position, current_direction = make_step(current_position, current_direction, action, count)
    return abs(current_position[0]) + abs(current_position[1])


if __name__ == '__main__':
    data = get_lines('in.txt')
    print(solve((0, 0), (10, 1), data))
