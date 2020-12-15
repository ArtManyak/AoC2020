def solve(turns, finish):
    last_turn_dict = {v: i for i, v in enumerate(turns[:-1], 1)}
    for cur_turn in range(len(turns), finish):
        new_val = 0 if turns[-1] not in last_turn_dict else cur_turn - last_turn_dict[turns[-1]]
        last_turn_dict[turns[-1]] = cur_turn
        turns.append(new_val)
    return turns[-1]


if __name__ == '__main__':
    start = [6, 4, 12, 1, 20, 0, 16]
    print(solve(start, 2020))
    print(solve(start, 30000000))
