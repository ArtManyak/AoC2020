from common.common import get_lines


def execute_command(acc: int, line: int) -> [int, int]:
    command = code[line]
    if command.startswith('nop'):
        return acc, line + 1
    elif command.startswith('acc'):
        return acc + int(command[4:]), line + 1
    else:
        return acc, line + int(command[4:])


def solve(code: [str]) -> [bool, int]:
    accumulator, current_line = 0, 0
    executed_lines = set()
    while (current_line not in executed_lines) and (current_line != len(code)):
        executed_lines.add(current_line)
        accumulator, current_line = execute_command(accumulator, current_line)

    return current_line == len(code), accumulator


def solve_2() -> int:
    fix = {'jmp': 'nop', 'nop': 'jmp'}
    for i in range(len(code)):
        command = code[i]
        if command[:3] in fix.keys():
            code[i] = command.replace(command[:3], fix[command[:3]])
            finished, acc = solve(code)
            if finished:
                return acc
            code[i] = command


code = get_lines('in.txt')
if __name__ == '__main__':
    print(solve(code))
    print(solve_2())
