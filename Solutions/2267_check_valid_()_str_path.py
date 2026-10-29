"""
2267. Check if There Is a Valid Parentheses String Path
Difficulty: Hard
Topic: Array, Dynamic Programming, Breadth-First Search, Matrix
Link: https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

Approach:
    Use BFS to explore paths from the top-left cell to the bottom-right cell.
    Track each state as (row, col, count), where count represents the
    current balance of opening and closing parentheses.
    Increase count for '(' and decrease it for ')'.
    If count becomes negative, discard the state because the path is invalid.
    Move only right or down, and use a visited set to avoid processing
    the same state more than once.
    Return True if the destination is reached with count == 0;
    otherwise, return False.

Complexity:
    Time:  O(m * n * min(m + n, 2 * min(m, n))) states in a tighter
           bound; commonly described as O(m * n * (m + n))
    Space: O(m * n * (m + n)) for the queue and visited set
"""

from collections import deque

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # A valid path must have an even number of cells
        if (m + n) % 2 == 1:
            return False

        directions = [(0, 1), (1, 0)]

        count = 1 if grid[0][0] == '(' else -1

        queue = deque([(0, 0, count)])
        visited = {(0, 0, count)}

        while queue:
            row, col, count = queue.popleft()

            if count < 0:
                continue

            if row == m - 1 and col == n - 1:
                if count == 0:
                    return True

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < m and 0 <= new_col < n:
                    if grid[new_row][new_col] == '(':
                        new_count = count + 1
                    else:
                        new_count = count - 1

                    # Prune states that cannot reach zero balance
                    remaining = (m - 1 - new_row) + (n - 1 - new_col)

                    if new_count > remaining:
                        continue

                    state = (new_row, new_col, new_count)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

        return False
