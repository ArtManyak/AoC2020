import re

from common.common import get_all_text


def is_correct(value, bound_dict):
    for bound in bound_dict:
        (min1, max1), (min2, max2) = bound_dict[bound]
        if min1 <= value <= max1 or min2 <= value <= max2:
            return True
    return False


def solve(bound_dict, tickets):
    invalid_values = []
    for ticket in tickets:
        values = [int(x) for x in ticket.split(',')]
        for value in values:
            if not is_correct(value, bound_dict):
                invalid_values.append(value)
    return sum(invalid_values)


def get_valid_tickets(bound_dict, tickets):
    valid_tickets = []
    for ticket in tickets:
        values = [int(x) for x in ticket.split(',')]
        is_valid = True
        for value in values:
            if not is_correct(value, bound_dict):
                is_valid = False
        if is_valid:
            valid_tickets.append(ticket)
    return valid_tickets


def solve2(bound_dict, my_ticket, valid_tickets):
    my_ticket_possible_rules = get_possible_rules(bound_dict, my_ticket)
    for valid_ticket in valid_tickets:
        valid_ticket_possible_rules = get_possible_rules(bound_dict, valid_ticket)
        for i in range(len(my_ticket_possible_rules)):
            my_ticket_possible_rules[i] = my_ticket_possible_rules[i].intersection(valid_ticket_possible_rules[i])

    while not all([len(x) == 1 for x in my_ticket_possible_rules]):
        next_vals = [x for x in my_ticket_possible_rules if len(x) == 1]
        for next_val in next_vals:
            for my_ticket_possible_rule in my_ticket_possible_rules:
                if len(next_val.intersection(my_ticket_possible_rule)) == 1 and len(my_ticket_possible_rule) != 1:
                    my_ticket_possible_rule.difference_update(next_val)

    result = 1
    my_ticket_values = [int(x) for x in my_ticket.split(',')]
    for (i, v) in enumerate(my_ticket_possible_rules):
        row_type = str([x for x in v][0])
        if row_type.startswith('departure'):
            result *= my_ticket_values[i]

    return result


def get_possible_rules(bound_dict, my_ticket):
    result = []
    for value in [int(x) for x in my_ticket.split(',')]:
        possible_rules = set()
        for bound in bound_dict:
            (min1, max1), (min2, max2) = bound_dict[bound]
            if min1 <= value <= max1 or min2 <= value <= max2:
                possible_rules.add(bound)
        result.append(possible_rules)
    return result


if __name__ == '__main__':
    boundaries, my_ticket, nearby_tickets = get_all_text('in.txt').split('\n\n')
    boundaries_parsed = {}
    for boundary in boundaries.split('\n'):
        match = re.match(r'(.*):(.*)-(.*) or (.*)-(.*)', boundary)
        boundaries_parsed[match.group(1)] = [(int(match.group(2)), int(match.group(3))), (int(match.group(4)), int(match.group(5)))]
    print(solve(boundaries_parsed, nearby_tickets.split('\n')[1:]))
    valid_tickets = get_valid_tickets(boundaries_parsed, nearby_tickets.split('\n')[1:])
    print(solve2(boundaries_parsed, my_ticket.split('\n')[1], valid_tickets))

