class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Modifies the given matrix in-place such that if an element is 0, 
        its entire row and column are set to 0.

        Time complexity: O(m * n)
        Space complexity: O(m + n)
        """
        # Get number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])

        # Arrays to mark rows and columns that need to be set to zero, initialized with -1 (indicating no zero encountered)
        row_mat = [-1] * rows
        col_mat = [-1] * cols

        # First pass: Identify rows and columns that should be set to zero
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_mat[i] = 0
                    col_mat[j] = 0

        # Second pass: Set entire row to zero if marked
        for i in range(rows):
            if row_mat[i] == 0:
                matrix[i] = [0] * cols
        
        # Third pass: Set entire column to zero if marked
        for j in range(cols):
            if col_mat[j] == 0:
                for row in range(rows):
                    matrix[row][j] = 0

# Example test case
Solution.setZeroes(Solution, [[1,1,1],[1,0,1],[1,1,1]])
# Expected Output: matrix = [[1,0,1],[0,0,0],[1,0,1]]
