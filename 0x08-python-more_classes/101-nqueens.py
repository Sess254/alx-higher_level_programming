#!/usr/bin/python3

import sys


def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []

    def safe(row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            j = row - i
            if col - j >= 0 and board[i][col - j] == 'Q':
                return False
            if col + j < N and board[i][col + j] == 'Q':
                return False
        return True

    def backtrck(row):
        if row == N:
            solutions.append([''.join(row) for row in board])
            return
        for col in range(N):
            if safe(row, col):
                board[row][col] = 'Q'
                backtrck(row + 1)
                board[row][col] = '.'

    backtrck(0)

    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
