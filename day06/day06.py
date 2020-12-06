from common.common import get_all_text


def solve() -> int:
    result = 0
    for group in groups:
        result += len(set(filter(lambda x: x != '\n', group)))
    return result


def solve_2() -> int:
    result = 0
    for group in groups:
        persons = group.split('\n')
        sets = list(map(set, persons))
        result += len(sets[0].intersection(*sets))
    return result


groups = get_all_text('in.txt').split('\n\n')
if __name__ == '__main__':
    print(solve())
    print(solve_2())
