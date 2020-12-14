import re

from common.common import get_lines


def apply_mask(mask, mem_value):
    bit_value = '{0:b}'.format(mem_value)
    bit_value = '0'*(len(mask) - len(bit_value)) + bit_value
    result = ''
    for i in range(len(mask)):
        if mask[i] == 'X':
            result += bit_value[i]
        else:
            result += mask[i]
    return int(result, 2)


def apply_mask2(mask, mem_value):
    bit_value = '{0:b}'.format(mem_value)
    bit_value = '0'*(len(mask) - len(bit_value)) + bit_value
    result = ['']
    for i in range(len(mask)):
        if mask[i] == '0':
            result = [x + bit_value[i] for x in result]
        elif mask[i] == '1':
            result = [x + '1' for x in result]
        else:
            result_copy = result
            result = [x + '0' for x in result]
            result_copy = [x + '1' for x in result_copy]
            for x in result_copy:
                result.append(x)
    return [int(x, 2) for x in result]


def solve(lines, apply_mask_func):
    mask = ''
    mem = {}
    for line in lines:
        if line.startswith('mask'):
            mask = line[7:-1]
        else:
            search = re.search(r'\[(.+)].*=(.+)', line)
            mem_index = int(search.group(1))
            mem_value = int(search.group(2))
            indicies = apply_mask_func(mask, mem_index)
            for i in indicies:
                mem[i] = mem_value
    return sum(mem[x] for x in mem)


if __name__ == '__main__':
    lines = get_lines('in.txt')
    # print(solve(lines, apply_mask))
    print(solve(lines, apply_mask2))
