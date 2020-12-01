#!/usr/bin/env python3

from itertools import combinations

def read_input():
    with open('input.txt') as f:
        puzzle_input = f.read().splitlines()
    puzzle_input = [int(entry) for entry in puzzle_input]
    return sorted(puzzle_input)

def part1(puzzle_input):
    for combination in combinations(puzzle_input, 2):
        if combination[0] + combination[1] == 2020:
            return combination[0] * combination[1]

def part2(puzzle_input):
    for combination in combinations(puzzle_input, 3):
        if combination[0] + combination[1] + combination[2]== 2020:
            return combination[0] * combination[1] * combination[2]

def main():
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()