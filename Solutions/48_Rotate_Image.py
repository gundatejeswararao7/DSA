class Solution:

    def reverse(self, mat, left, right):
        while left <= right:
            mat[left], mat[right] = mat[right], mat[left]
            left += 1
            right -= 1

    def rotate(self, matrix):
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for row in matrix:
            self.reverse(row, 0, n - 1)
