from common.common import get_numbers


def solve() -> int:
    numbers = get_numbers('in.txt')
    dictionary = {i: 1 for i in numbers}
    for i in numbers:
        for j in numbers:
            k = 2020 - i - j
            if k in dictionary:
                return i * j * k


if __name__ == '__main__':
    print(solve())
