"""
Maximum Distance Between K Points
Difficulty: Hard
Topic: Array, Sorting, Binary Search, Greedy
Link: Custom problem link not confirmed

Approach:
    Convert each boundary point into a one-dimensional coordinate along
    the square's perimeter, moving clockwise from (0, 0).
    Sort the coordinates and extend the array by adding the perimeter
    length P to each coordinate to handle circular distances.
    Use binary search to find the maximum possible minimum distance D.
    The feasible() function checks whether k points can be selected
    with every pair of consecutive selected points at least D apart.
    Use a next-index array to greedily find the next valid point.
    Finally, check the wraparound distance between the last selected
    point and the starting point.

Complexity:
    Time:  O(n^2 log P), where n is the number of points and P = 4 * side
    Space: O(n) auxiliary space
"""

from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Map each point to its clockwise perimeter coordinate
        P = 4 * side
        t = []

        for x, y in points:
            if y == 0 and 0 <= x <= side:
                t.append(x)
            elif x == side and 0 <= y <= side:
                t.append(side + y)
            elif y == side and 0 <= x <= side:
                t.append(2 * side + (side - x))
            else:
                t.append(3 * side + (side - y))

        t.sort()
        n = len(t)
        t_ext = t + [x + P for x in t]

        # Check whether k points can be selected with minimum distance D
        def feasible(D: int) -> bool:
            if D == 0:
                return True

            m = len(t_ext)
            nxt = [-1] * m
            j = 0

            # Find the next point at least D away
            for i in range(m):
                if j <= i:
                    j = i + 1

                while j < m and t_ext[j] - t_ext[i] < D:
                    j += 1

                if j < m:
                    nxt[i] = j

            # Try every point as the starting point
            for start in range(n):
                cur = start
                cnt = 1

                while cnt < k:
                    nxt_idx = nxt[cur]

                    if nxt_idx == -1 or nxt_idx >= start + n:
                        break

                    cur = nxt_idx
                    cnt += 1

                if cnt == k:
                    # Check the circular distance back to the start
                    if t_ext[cur] - t_ext[start] <= P - D:
                        return True

            return False

        # Binary search for the maximum minimum distance
        lo, hi = 0, P

        while lo < hi:
            mid = (lo + hi + 1) // 2

            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
