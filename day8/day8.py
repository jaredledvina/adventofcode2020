#!/usr/bin/env python3
import json


def read_input():
    with open('input.txt') as f:
        puzzle_input = f.read().splitlines()
    parsed = []
    for entry in puzzle_input:
        action, change = entry.split(' ')
        parsed.append((action, int(change)))
    return parsed

def part1(puzzle_input):
    seen = []
    accumulator = 0
    position = 0
    while position not in seen:
        entry = puzzle_input[position]
        seen.append(position)
        if entry[0] == 'acc':
            accumulator += entry[1]
            position += 1
        elif entry[0] == 'jmp':
            position += entry[1]
        elif entry[0] == 'nop':
            position += 1
    return accumulator

def debugger(puzzle_input, swap=True):
    seen = []
    accumulator = 0
    position = 0
    while position not in seen:
        try:
            entry = puzzle_input[position]
        except IndexError:
            return accumulator, True
        seen.append(position)
        if entry[0] == 'acc':
            accumulator += entry[1]
            position += 1
        elif entry[0] == 'jmp':
            if swap:
                test_nop = puzzle_input.copy()
                test_nop[position] = ('nop', puzzle_input[position][1])
                acc, winner = debugger(test_nop, False)
                if winner:
                    return acc
                    break
            position += entry[1]
        elif entry[0] == 'nop':
            if swap:
                test_jmp = puzzle_input.copy()
                test_jmp[position] = ('jmp', puzzle_input[position][1])
                acc, winner = debugger(test_jmp, False)
                if winner:
                    return acc
                    break
            position += 1
    return accumulator, False

def part2(puzzle_input):
    return debugger(puzzle_input)
   
def main():
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()