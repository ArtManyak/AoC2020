import re

from common.common import get_all_text


def build_dict(passport: str):
    parts = passport.split()
    return dict(map(lambda x: x.split(':'), parts))


def solve() -> int:
    result = 0
    necessary_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        passport_dict = build_dict(passport)
        if any(k not in passport_dict for k in necessary_fields):
            continue
        byr = int(passport_dict['byr'])
        iyr = int(passport_dict['iyr'])
        eyr = int(passport_dict['eyr'])
        if byr < 1920 or byr > 2002 or iyr < 2010 or iyr > 2020 or eyr < 2020 or eyr > 2030:
            continue
        regex = re.search('([0-9]+)(.*)', passport_dict['hgt'])
        hgt, hgt_s = int(regex.group(1)), regex.group(2)
        if (hgt_s == 'cm' and (hgt < 150 or hgt > 193)) or (hgt_s == 'in' and (hgt < 59 or hgt > 76)) or hgt_s not in (
        'cm', 'in'):
            continue
        if not re.match('^#[0-9a-f]{6}$', passport_dict['hcl']):
            continue
        if passport_dict['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue
        if not re.match('^[0-9]{9}$', passport_dict['pid']):
            continue
        result += 1

    return result


passports = get_all_text('in.txt').split('\n\n')
if __name__ == '__main__':
    print(solve())
