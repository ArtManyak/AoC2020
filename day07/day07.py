import re

from common.common import get_lines


def solve(start_bag: str) -> int:
    viewed_bags.add(start_bag)
    next_bags = list(
        filter(
            lambda x: x not in viewed_bags,
            map(
                lambda x: ' '.join(x.split(' ')[:2]),
                filter(
                    lambda x: start_bag in x and not x.startswith(start_bag),
                    data
                )
            )
        )
    )
    return len(next_bags) + sum(map(solve, next_bags))


def solve_2(start_bag: str) -> int:
    cur_line = next(x for x in data if x.startswith(start_bag))
    next_bags = re.findall('([0-9]+ [a-z]+ [a-z]+)', cur_line)
    result = 0
    for next_bag in next_bags:
        mult = int(next_bag.split(' ')[0])
        bag = ' '.join(next_bag.split(' ')[1:])
        result += mult + mult * solve_2(bag)
    return result


data = get_lines('in.txt')
viewed_bags = set()
if __name__ == '__main__':
    print(solve('shiny gold'))
    print(solve_2('shiny gold'))
