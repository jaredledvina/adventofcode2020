#!/usr/bin/env python3
import itertools

def read_input():
    with open('input.txt') as f:
        puzzle_input = f.read().splitlines()
        puzzle_input = [int(num) for num in puzzle_input]
    return puzzle_input

def part1(puzzle_input):
    preamble = puzzle_input[:25]
    remaining = puzzle_input[25:]
    for item in remaining:
        found_match = False
        for product in itertools.product(preamble, preamble):
            if product[0] + product[1] == item:
                found_match = True
                preamble.append(item)
                preamble.pop(0)
                break
        if not found_match:
            return item

def part2(puzzle_input):
    invalid = part1(puzzle_input)
    for position in range(len(puzzle_input)):
        combination_position = 0
        for combination in itertools.accumulate(puzzle_input[position:]):
            if combination == invalid:
                return min(puzzle_input[position:combination_position+position]) + max(puzzle_input[position:combination_position+position])
            combination_position += 1
        


   
def main():
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()