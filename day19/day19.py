import re

from common.common import get_all_text


def get_regexp(rules):
    rules_dict = dict()
    for rule in rules.split('\n'):
        rule_number, rule_content = rule.split(':')
        rules_dict[rule_number] = f'{rule_content} '.replace('"', '')
    rules_dict['8'] = '( 42 )+'
    while any(x.isdigit() for x in rules_dict['0']):
        next_rules = set([x for x in rules_dict['0'].split(' ') if x.isdigit()])
        for next_rule in next_rules:
            if next_rule == '11':
                hack_rule = ' | '.join(' ( ' + ' 42 ' * i + ' 31 ' * i + ' ) ' for i in range(1, 6))
                rules_dict['0'] = rules_dict['0'].replace(f' {next_rule} ', f' ( {hack_rule} ) ')
            else:
                rules_dict['0'] = rules_dict['0'].replace(f' {next_rule} ', ' ( ' + rules_dict[next_rule] + ' ) ')

    return rules_dict['0'].replace(' ', '')


if __name__ == '__main__':
    rules, messages = get_all_text('in.txt').split('\n\n')
    regexp = get_regexp(rules)
    print(len([x for x in messages.split('\n') if re.fullmatch(rf'{regexp}', x)]))
