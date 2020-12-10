from typing import List

from common.common import get_lines


def solve(jolts: List[int]) -> int:
    dif_1, dif_3 = 0, 0
    for i in range(len(jolts) - 1):
        diff = jolts[i + 1] - jolts[i]
        dif_1 += 1 if diff == 1 else 0
        dif_3 += 1 if diff == 3 else 0
    return dif_1 * dif_3


def solve_2(jolts: List[int], i: int, dp) -> int:
    if i in dp:
        return dp[i]
    dp[i] = sum(solve_2(jolts, i - j, dp) for j in range(1, 4) if i - j >= 0 and jolts[i] - jolts[i - j] <= 3)
    return dp[i]


if __name__ == '__main__':
    numbers = list(map(int, get_lines('in.txt')))
    numbers.extend([0, max(numbers) + 3])
    numbers.sort()
    print(solve(numbers))
    dp = {0: 1}
    print(solve_2(numbers, len(numbers) - 1, dp))
