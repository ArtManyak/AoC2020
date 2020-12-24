import copy

from common.common import get_lines


class Tile:
    def __init__(self, q, r, s):
        self.q = q
        self.r = r
        self.s = s
        self.color = 'White'

    def flip(self):
        self.color = 'White' if self.color == 'Black' else 'Black'


def walk_through(tiles, tile, route):
    while len(route) != 0:
        if route.startswith('e'):
            if (tile.q + 1, tile.r, tile.s - 1) not in tiles:
                tiles[(tile.q + 1, tile.r, tile.s - 1)] = Tile(tile.q + 1, tile.r, tile.s - 1)
            tile = tiles[(tile.q + 1, tile.r, tile.s - 1)]
            route = route[1:]
        elif route.startswith('se'):
            if (tile.q, tile.r + 1, tile.s - 1) not in tiles:
                tiles[(tile.q, tile.r + 1, tile.s - 1)] = Tile(tile.q, tile.r + 1, tile.s - 1)
            tile = tiles[(tile.q, tile.r + 1, tile.s - 1)]
            route = route[2:]
        elif route.startswith('sw'):
            if (tile.q - 1, tile.r + 1, tile.s) not in tiles:
                tiles[(tile.q - 1, tile.r + 1, tile.s)] = Tile(tile.q - 1, tile.r + 1, tile.s)
            tile = tiles[(tile.q - 1, tile.r + 1, tile.s)]
            route = route[2:]
        elif route.startswith('w'):
            if (tile.q - 1, tile.r, tile.s + 1) not in tiles:
                tiles[(tile.q - 1, tile.r, tile.s + 1)] = Tile(tile.q - 1, tile.r, tile.s + 1)
            tile = tiles[(tile.q - 1, tile.r, tile.s + 1)]
            route = route[1:]
        elif route.startswith('nw'):
            if (tile.q, tile.r - 1, tile.s + 1) not in tiles:
                tiles[(tile.q, tile.r - 1, tile.s + 1)] = Tile(tile.q, tile.r - 1, tile.s + 1)
            tile = tiles[(tile.q, tile.r - 1, tile.s + 1)]
            route = route[2:]
        else:
            if (tile.q + 1, tile.r - 1, tile.s) not in tiles:
                tiles[(tile.q + 1, tile.r - 1, tile.s)] = Tile(tile.q + 1, tile.r - 1, tile.s)
            tile = tiles[(tile.q + 1, tile.r - 1, tile.s)]
            route = route[2:]
    tile.flip()


def get_neighbours(tile):
    (q, r, s) = tile
    return [(q + 1, r, s - 1), (q, r + 1, s - 1), (q - 1, r + 1, s), (q - 1, r, s + 1), (q, r - 1, s + 1),
            (q + 1, r - 1, s)]


def simulate_life(tiles):
    new_tiles = copy.deepcopy(tiles)
    for tile in tiles:
        neighbours = get_neighbours(tile)
        for neighbour in neighbours:
            if neighbour not in new_tiles:
                q, r, s = neighbour
                new_tiles[neighbour] = Tile(q, r, s)

    for tile in new_tiles:
        neighbours = get_neighbours(tile)
        black = sum(1 for neighbour in neighbours if neighbour in tiles and tiles[neighbour].color == 'Black')
        if tile in tiles and tiles[tile].color == 'Black' and (black == 0 or black > 2):
            new_tiles[tile].flip()
        elif (tile not in tiles or tiles[tile].color == 'White') and black == 2:
            new_tiles[tile].flip()
    return new_tiles


if __name__ == '__main__':
    lines = get_lines('in.txt')
    start_tile = Tile(0, 0, 0)
    tiles = {(0, 0, 0): start_tile}
    for line in lines:
        walk_through(tiles, start_tile, line)
    print(sum(1 for x in tiles if tiles[x].color == 'Black'))

    for i in range(100):
        if i % 10 == 0:
            print('iteration: ', i)
        tiles = simulate_life(tiles)
    print(sum(1 for x in tiles if tiles[x].color == 'Black'))
