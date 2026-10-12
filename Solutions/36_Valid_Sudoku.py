"""
36. Valid Sudoku
Difficulty: Medium
Topic: Array, Hash Table, Matrix
Link: https://leetcode.com/problems/valid-sudoku

Approach 1: Using Sets
    Check each row, column, and 3x3 box using a set.
    If a digit already exists in the corresponding set, return False.
    Ignore '.' because it represents an empty cell.
    If no duplicates are found, return True.

Complexity:
    Time:  O(n^2)
    Space: O(n)

Approach 2: Checking Each Existing Number
    Visit every cell containing a digit. Temporarily replace the digit
    with '.' to avoid detecting itself as a duplicate. Check its row,
    column, and 3x3 box for the same digit. If a duplicate is found,
    return False. Otherwise, restore the digit and continue.

Complexity:
    Time:  O(1) for a fixed 9x9 board
    Space: O(1) auxiliary space
"""

# Approach 1: Using Sets
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # Check rows
        for r in range(n):
            row_vals = set()
            for c in range(n):
                val = board[r][c]
                if val != ".":
                    if val in row_vals:
                        return False
                    row_vals.add(val)

        # Check columns
        for c in range(n):
            col_vals = set()
            for r in range(n):
                val = board[r][c]
                if val != ".":
                    if val in col_vals:
                        return False
                    col_vals.add(val)

        # Check 3x3 boxes
        for box_row in range(0, n, 3):
            for box_col in range(0, n, 3):
                box_vals = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        val = board[r][c]
                        if val != ".":
                            if val in box_vals:
                                return False
                            box_vals.add(val)

        return True


# Approach 2: Checking Each Existing Number
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def IsValidSudoku(board, row, column, num):
            # Check row and column
            for i in range(9):
                if board[row][i] == num or board[i][column] == num:
                    return False

            # Check 3x3 box
            start_row = 3 * (row // 3)
            start_col = 3 * (column // 3)

            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False

            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    board[i][j] = '.'

                    if not IsValidSudoku(board, i, j, num):
                        return False

                    board[i][j] = num

        return True
