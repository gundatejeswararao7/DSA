"""
Maximum Weight of Non-Overlapping Intervals
Difficulty: Hard
Topic: Array, Dynamic Programming, Sorting, Binary Search
Link: Custom problem link not confirmed

Approach:
    Store each interval as (start, end, weight, original_index) and sort
    the intervals by start time.
    Use binary search to find the first interval starting after the
    current interval's end time.
    Define dp[i][k] as the best result considering intervals from i onward
    with at most k intervals remaining.
    For each interval, compare two options:
        Skip: Use dp[i + 1][k].
        Take: Add its weight to dp[next_i][k - 1].
    Store both the total weight and sorted original indices.
    Prefer the greater weight; if weights are equal, prefer the
    lexicographically smaller index tuple.
    Return the selected original indices.

Complexity:
    Time:  O(n log n + n * 4 * log n + n * 4 * k log k)
           where k <= 4 is the maximum number of selected intervals
    Space: O(n * 4 * k) for the DP states and stored index tuples
"""

from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Store (start, end, weight, original_index)
        ext = [
            (intervals[i][0], intervals[i][1], intervals[i][2], i)
            for i in range(n)
        ]

        # Sort by start time
        ext.sort(key=lambda x: x[0])
        starts = [x[0] for x in ext]

        # Find the first interval with start_time > target_r
        def get_next_idx(target_r: int) -> int:
            low, high = 0, n

            while low < high:
                mid = (low + high) // 2

                if starts[mid] > target_r:
                    high = mid
                else:
                    low = mid + 1

            return low

        # dp[i][k] = (maximum weight, selected original indices)
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        def is_better(opt1, opt2):
            w1, idx1 = opt1
            w2, idx2 = opt2

            if w1 != w2:
                return w1 > w2

            return idx1 < idx2

        # Bottom-up dynamic programming
        for i in range(n - 1, -1, -1):
            curr_l, curr_r, weight, orig_idx = ext[i]
            next_i = get_next_idx(curr_r)

            for k in range(1, 5):
                # Option 1: Skip the current interval
                skip_option = dp[i + 1][k]

                # Option 2: Take the current interval
                take_weight, take_indices = dp[next_i][k - 1]

                combined_indices = tuple(
                    sorted((orig_idx,) + take_indices)
                )
                take_option = (weight + take_weight, combined_indices)

                if is_better(take_option, skip_option):
                    dp[i][k] = take_option
                else:
                    dp[i][k] = skip_option

        return list(dp[0][4][1])
