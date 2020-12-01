from typing import List


def getNumbers(file_path: str) -> List[int]:
    with open(file_path) as file:
        return list(map(int, file.readlines()))
