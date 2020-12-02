#!/usr/bin/env python3
from collections import Counter

def read_input():
    with open('input.txt') as f:
        puzzle_input = f.read().splitlines()
    return sorted(puzzle_input)

def part1(puzzle_input):
    valid_passwords = 0
    for entry in puzzle_input:
        digits, letter, password = entry.replace(':', '').split(' ')
        start, end = digits.split('-')
        counted = Counter(password)
        if counted[letter] >= int(start) and counted[letter] <= int(end):
            valid_passwords += 1
    return valid_passwords

def part2(puzzle_input):
    valid_passwords = 0
    for entry in puzzle_input:
        digits, letter, password = entry.replace(':', '').split(' ')
        start, end = digits.split('-')
        if password[int(start)-1] == letter and not password[int(end)-1] == letter:
            valid_passwords += 1
        elif password[int(start)-1] != letter and password[int(end)-1] == letter:
            valid_passwords += 1
    return valid_passwords

def main():
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
