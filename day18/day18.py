from common.common import get_lines


def eval_simple(parts):
    result = int(parts[0])
    cur_i = 0
    while cur_i + 2 < len(parts):
        if parts[cur_i + 1] == '+':
            result += int(parts[cur_i + 2])
        else:
            result *= int(parts[cur_i + 2])
        cur_i += 2
    return result


def eval_hard(parts):
    while '+' in parts:
        plus_index = parts.index('+')
        parts = [*parts[:plus_index - 1], int(parts[plus_index - 1]) + int(parts[plus_index + 1]), *parts[plus_index + 2:]]
    while '*' in parts:
        mul_index = parts.index('*')
        parts = [*parts[:mul_index - 1], int(parts[mul_index - 1]) * int(parts[mul_index + 1]), *parts[mul_index + 2:]]
    return parts[0]


def execute(line, eval_func):
    parts = [x for x in '({})'.format(line).replace('(', ' ( ').replace(')', ' ) ').split(' ') if x != '']
    stack = []
    for part in parts:
        if part == ')':
            to_eval = []
            cur_val = stack.pop()
            while cur_val != '(':
                to_eval.append(cur_val)
                cur_val = stack.pop()
            stack.append(eval_func(to_eval[::-1]))
        else:
            stack.append(part)
    return stack[0]


def solve(expressions, eval_func):
    return sum([execute(expr, eval_func) for expr in expressions])


if __name__ == '__main__':
    lines = get_lines('in.txt')
    print(solve(lines, eval_simple))
    print(solve(lines, eval_hard))
