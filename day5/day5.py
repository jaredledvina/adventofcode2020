#!/usr/bin/env python3

def read_input():
    with open('input.txt') as f:
        puzzle_input = f.read().splitlines()
    return puzzle_input


def get_ticket_id(ticket):
    max_row = 127
    min_row = 0
    max_column = 7
    min_column = 0
    for position in ticket:
        remaining_row = int(len(range(min_row, max_row + 1)) / 2)
        remaining_column = int(len(range(min_column, max_column + 1)) / 2)
        if position == "F":
            max_row = max_row - remaining_row
        elif position == "B":
            min_row = min_row + remaining_row
        elif position == "L":
            max_column = max_column - remaining_column
        elif position == "R":
            min_column = min_column + remaining_column
        else:
            print('wtf')
    return max_row * 8 + max_column

def part1(puzzle_input):
    max_ticket = 0
    for ticket in puzzle_input:
        ticket_id = get_ticket_id(ticket)
        if ticket_id > max_ticket:
            max_ticket = ticket_id
    return max_ticket

def part2(puzzle_input):
    tickets = []
    for ticket in puzzle_input:
        tickets.append(get_ticket_id(ticket))
    tickets = sorted(tickets)
    for entry in range(tickets[0], tickets[-1] + 1):
        if entry not in tickets:
            return entry

def main():
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()