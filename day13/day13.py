from common.common import get_lines


def solve(arrive_time, bus_ids):
    nex_times = {id: (arrive_time // id) * id + id for id in bus_ids}
    bus_id = min(nex_times, key=nex_times.get)
    return (nex_times[bus_id] - arrive_time) * bus_id


def reverse(x, mod):
    return x ** (mod - 2) % mod


def solve_2(bus_ids_with_shift):
    x = [0] * len(bus_ids_with_shift)
    result = 0
    m = 1
    for i in range(len(bus_ids_with_shift)):
        x[i] = bus_ids_with_shift[i][0] - bus_ids_with_shift[i][1]
        for j in range(i):
            x[i] = reverse(bus_ids_with_shift[j][0], bus_ids_with_shift[i][0]) * (x[i] - x[j])
            x[i] = (x[i] % bus_ids_with_shift[i][0] + bus_ids_with_shift[i][0]) % bus_ids_with_shift[i][0]
        result += x[i] * m
        m *= bus_ids_with_shift[i][0]
    return result


if __name__ == '__main__':
    lines = get_lines('in.txt')
    arrive_time = int(lines[0])
    bus_ids = [int(x) for x in lines[1].split(',') if x != 'x']
    print(solve(arrive_time, bus_ids))

    buses = lines[1].split(',')
    bus_ids_with_shift = [(int(buses[i]), i) for i in range(len(buses)) if buses[i] != 'x']
    print(solve_2(bus_ids_with_shift))
