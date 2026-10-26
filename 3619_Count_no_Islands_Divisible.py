"""
Count Islands With Sum Divisible by K
Difficulty: Medium
Topic: Array, Matrix, Graph, BFS, Connected Components
Link: https://leetcode.com/

Approach:
    Traverse every cell in the grid.
    If a cell contains a non-zero value, start a new island using BFS.
    Use a list as a queue to visit all four-directionally connected
    non-zero cells.
    Add each visited cell's value to total and mark it as 0 to avoid
    counting it again.
    After exploring the island, check whether total % k == 0.
    If true, increment ans.
    Return the total number of qualifying islands.

Complexity:
    Time:  O(m * n), where m and n are the grid dimensions
    Space: O(m * n) in the worst case for the BFS queue
"""

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue

                total = grid[i][j]
                grid[i][j] = 0
                island = [(i, j)]

                for x, y in island:
                    for a, b in (
                        (x + 1, y),
                        (x - 1, y),
                        (x, y + 1),
                        (x, y - 1)
                    ):
                        if 0 <= a < m and 0 <= b < n and grid[a][b]:
                            total += grid[a][b]
                            grid[a][b] = 0
                            island.append((a, b))

                if total % k == 0:
                    ans += 1

        return ans
