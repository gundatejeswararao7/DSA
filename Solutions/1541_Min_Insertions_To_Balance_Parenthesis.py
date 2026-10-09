"""
1541. Minimum Insertions to Balance a Parentheses String

Difficulty: Medium

Topic: Stack, Greedy

Link: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/


Approach:
    Use a stack to track unmatched opening parentheses and res to count
    required insertions. Each '(' needs two consecutive ')' characters.
    For every ')', check whether the next character is also ')'. If so,
    consume both; otherwise, count one insertion to complete the pair.
    If there is no unmatched '(', insert an opening '(' as needed.
    Finally, each unmatched '(' requires two closing parentheses.

Complexity:
    Time:  O(n)
    Space: O(n)
"""

class Solution(object):
    def minInsertions(self, s):
        st = []
        res = 0
        i = 0

        while i < len(s):
            ch = s[i]

            if ch == '(':
                st.append(ch)
            else:
                if not st:
                    if i < len(s) - 1 and s[i + 1] == ')':
                        i += 1
                    else:
                        res += 1
                    res += 1
                else:
                    if i < len(s) - 1 and s[i + 1] == ')':
                        i += 1
                    else:
                        res += 1
                    st.pop()

            i += 1

        return res + len(st) * 2