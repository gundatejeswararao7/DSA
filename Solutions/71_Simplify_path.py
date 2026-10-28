"""
71. Simplify Path
Difficulty: Medium
Topic: String, Stack
Link: https://leetcode.com/problems/simplify-path/

Approach:
    Split the path using '/' to process each directory component.
    Ignore empty components and "." because they do not change the path.
    If the component is "..", pop the last directory from the stack
    if one exists.
    Otherwise, push the directory name onto the stack.
    Join the stack elements with '/' and add a leading '/' to return
    the simplified absolute path.

Complexity:
    Time:  O(n), where n is the length of the path
    Space: O(n) for the stack and split components
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for i in path:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return "/" + "/".join(stack)
