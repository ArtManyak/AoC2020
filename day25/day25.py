from common.common import get_lines


def find_loop_size(val, public):
    result = 0
    tmp = 1
    while tmp != public:
        tmp = (tmp * val) % 20201227
        result += 1
    return result


def make_loop(cnt, val):
    tmp = 1
    for _ in range(cnt):
        tmp = (tmp * val) % 20201227
    return tmp


if __name__ == '__main__':
    card_public, door_public = [int(x) for x in get_lines('in.txt')]
    card_val, door_val = 7, 7
    card_loop = find_loop_size(card_val, card_public)
    door_loop = find_loop_size(door_val, door_public)

    print(make_loop(door_loop, card_public), make_loop(card_loop, door_public))
