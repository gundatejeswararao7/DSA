class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for char in s:
            if char == "(":
                stack.append(0)
            else:
                val = stack.pop()
                if val == 0:
                    score = 1
                else:
                    score = 2*val
                stack[-1] += score
        return stack[-1]
