"""
2409. Count Days Spent Together
Difficulty: Easy
Topic: String, Simulation
Link: https://leetcode.com/problems/count-days-spent-together/

Approach:
    Convert each date into an integer in MMDD format for easy
    comparison.

    Iterate through every day of the year, using the number of
    days in each month. For each day, check whether it falls
    within both Alice's and Bob's arrival and departure dates.

    If the day is within both intervals, increment the answer.
    Return the total number of days they spent together.

Complexity:
    Time:  O(1)   # At most 365 days are checked
    Space: O(1)   # Fixed-size list of month lengths
"""

class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str,
        arriveBob: str, leaveBob: str
    ) -> int:
        def date_key(date: str) -> int:
            return int(date[:2]) * 100 + int(date[3:])

        a_start = date_key(arriveAlice)
        a_end = date_key(leaveAlice)
        b_start = date_key(arriveBob)
        b_end = date_key(leaveBob)

        days_in_month = [
            31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31
        ]

        answer = 0

        for month, length in enumerate(days_in_month, start=1):
            for day in range(1, length + 1):
                current = month * 100 + day

                if (
                    a_start <= current <= a_end
                    and b_start <= current <= b_end
                ):
                    answer += 1

        return answer
