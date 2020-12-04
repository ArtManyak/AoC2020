from typing import List


def get_numbers(file_path: str) -> List[int]:
    with open(file_path) as file:
        return list(map(int, file.readlines()))


def get_lines(file_path: str) -> List[str]:
    with open(file_path) as file:
        return file.readlines()


def get_all_text(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()
