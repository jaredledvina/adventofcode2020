#!/usr/bin/env python3

def read_input():
    with open('input.txt') as f:
        puzzle_input = f.read().splitlines()
    return puzzle_input

def part1(puzzle_input):
    group_answers = set()
    answers = 0
    for entry in puzzle_input:
        if entry != '':
            for answer in entry:
                group_answers.add(answer)
        else:
            answers =+ answers + len(group_answers)
            group_answers = set()
    answers =+ answers + len(group_answers)
    return answers

def part2(puzzle_input):
    group = []
    people = 0
    answers = 0
    for entry in puzzle_input:
        if entry != '':
            people += 1
            for answer in entry:
                group.append(answer)
        else:
            for answer in set(group):
                if group.count(answer) == people:
                    answers += 1
            group = []
            people = 0
    for answer in set(group):
        if group.count(answer) == people:
            answers += 1
    return answers

def main():
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()