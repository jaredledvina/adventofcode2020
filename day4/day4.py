#!/usr/bin/env python3

def read_input():
    with open('input.txt') as f:
        puzzle_input = f.read().splitlines()
    return puzzle_input

def eval_passport(passport):
    required = [ 'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid']
    for attr in required:
        if attr not in passport:
            return False
    return True

def eval_passport_complex(passport):
    if not eval_passport(passport):
        return False
    for entry in passport.split(' '):
        split_entry = entry.split(':')
        field = split_entry[0]
        value = split_entry[1]
        if field == 'byr':
            if len(value) != 4 or not value.isdigit() or int(value) not in range(1920, 2002 + 1):
                return False
        if field == 'iyr':
            if len(value) != 4 or not value.isdigit() or int(value) not in range(2010, 2020 + 1):
                return False
        if field == 'eyr':
            if len(value) != 4 or not value.isdigit() or int(value) not in range(2020, 2030 + 1):
                return False
        if field == 'hgt':
            if 'cm' in value:
                height = value.split('cm')[0]
                if int(height) not in range(150, 193 + 1):
                    return False
            elif 'in' in value:
                height = value.split('in')[0]
                if int(height) not in range(59, 76 + 1):
                    return False
            else:
                return False
        if field == 'hcl':
            if value[0] != '#':
                return False
            if len(value[1:]) == 6:
                for item in value[1:]:
                    if item.isdigit():
                        if int(item) not in range(0, 9 + 1):
                            return False
                    elif item not in ['a', 'b', 'c', 'd', 'e','f']:
                        return False
            else: 
                return False
        if field == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        if field == 'pid':
            if not value.isdigit() or not len(value) == 9:
                return False
    return True

def part1(puzzle_input):
    valid_passports = 0
    current_passport = ""
    for entry in puzzle_input:
        if entry != "":
            current_passport = current_passport + " " + entry
        else:
            if eval_passport(current_passport):
                valid_passports += 1
            current_passport = ""
    if eval_passport(current_passport):
        valid_passports += 1
    return valid_passports

def part2(puzzle_input):
    valid_passports = 0
    current_passport = ""
    for entry in puzzle_input:
        if entry != "":
            current_passport = current_passport + " " + entry
        else:
            if eval_passport_complex(current_passport.strip()):
                valid_passports += 1
            current_passport = ""
    if eval_passport_complex(current_passport.strip()):
        valid_passports += 1
    return valid_passports

def main():
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()