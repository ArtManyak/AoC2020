from typing import List

from common.common import get_lines


def find_terms(number: int, numbers_part: List[int]) -> bool:
    for i in range(len(numbers_part)):
        for j in range(i + 1, len(numbers_part)):
            if numbers_part[i] + numbers_part[j] == number:
                return True
    return False


def solve(numbers: List[int], preamble_len: int) -> int:
    for i in range(preamble_len, len(numbers)):
        if not find_terms(numbers[i], numbers[i - preamble_len:i]):
            return numbers[i]
    return 0


def solve_2(numbers: List[int], value: int) -> int:
    cur_sum = 0
    i, j = 0, 0
    while cur_sum != value:
        if cur_sum < value:
            cur_sum += numbers[j]
            j += 1
        if cur_sum > value:
            cur_sum -= numbers[i]
            i += 1
    return min(numbers[i:j]) + max(numbers[i:j])


if __name__ == '__main__':
    numbers = list(map(int, get_lines('in.txt')))
    corrupted_value = solve(numbers, 25)
    print(corrupted_value)
    print(solve_2(numbers, corrupted_value))
