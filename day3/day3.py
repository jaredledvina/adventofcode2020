#!/usr/bin/env python3

def read_input():
    with open('input.txt') as f:
        puzzle_input = f.read().splitlines()
    return puzzle_input

def move(puzzle_input, x, y, x_move, y_move):
    trees = 0 
    while y < len(puzzle_input):
        if x > len(puzzle_input[abs(y)]):
            for line in range(len(puzzle_input)):
                puzzle_input[line] = puzzle_input[line] + puzzle_input[line]
        if puzzle_input[y][x] == "#":
            trees += 1
        x = x + x_move
        y = y + y_move
    return trees

def part1(puzzle_input):
    return move(puzzle_input, 0, 0, 3, 1)

def part2(puzzle_input):
    a = move(puzzle_input, 0, 0, 1, 1) 
    b = move(puzzle_input, 0, 0, 3, 1) 
    c = move(puzzle_input, 0, 0, 5, 1) 
    d = move(puzzle_input, 0, 0, 7, 1) 
    e = move(puzzle_input, 0, 0, 1, 2) 
    return a * b * c * d * e

def main():
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()