from common.common import get_lines


def parse_line(line: str) -> (int, int, str, str):
    policy, password = line.split(':')
    min_max, letter = policy.split(' ')
    lower_bound, upper_bound = map(int, min_max.split('-'))
    return lower_bound, upper_bound, letter, password


def solve() -> int:
    lines = get_lines('in.txt')
    return len(list(filter(is_valid_pass, lines)))


def is_valid_pass(line: str) -> bool:
    lower_bound, upper_bound, letter, password = parse_line(line)
    return lower_bound <= password.count(letter) <= upper_bound


def solve2() -> int:
    lines = get_lines('in.txt')
    return len(list(filter(is_valid_pass2, lines)))


def is_valid_pass2(line: str) -> bool:
    lower_bound, upper_bound, letter, password = parse_line(line)
    return (password[lower_bound] == letter) ^ (password[upper_bound] == letter)


if __name__ == '__main__':
    print(solve())
    print(solve2())
