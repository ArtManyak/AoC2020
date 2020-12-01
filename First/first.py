from Common.common import getNumbers


def solve() -> int:
    numbers = getNumbers('in.txt')
    dictionary = {i: 1 for i in numbers}
    for i in numbers:
        for j in numbers:
            k = 2020 - i - j
            if k in dictionary:
                return i * j * k


if __name__ == '__main__':
    print(solve())
