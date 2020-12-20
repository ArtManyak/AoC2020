from functools import reduce

from common.common import get_all_text


class Tile:
    def __init__(self, lines):
        self.tile_title = lines.split('\n')[0].split(' ')[1][:-1]
        self.tile_lines = lines.split('\n')[1:]
        bl = ''.join(x[0] for x in self.tile_lines)
        br = ''.join(x[-1] for x in self.tile_lines)
        self.tile_borders = {self.tile_lines[0], self.tile_lines[0][::-1], self.tile_lines[-1],
                             self.tile_lines[-1][::-1], bl, bl[::-1], br, br[::-1]}


if __name__ == '__main__':
    input = get_all_text('in.txt').split('\n\n')
    tiles = [Tile(x) for x in input]
    intersections = {}
    for i in tiles:
        intersections[i.tile_title] = []
        for j in tiles:
            if i == j:
                continue
            if i.tile_borders.intersection(j.tile_borders):
                intersections[i.tile_title].append(j.tile_title)
    corners = [int(x) for x in intersections if len(intersections[x]) == 2]
    print(reduce(lambda x, y: x * y, corners))
