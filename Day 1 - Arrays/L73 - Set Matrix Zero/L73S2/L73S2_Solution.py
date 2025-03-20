class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None: 
        """
        Modifies the given matrix in-place such that if an element is 0, 
        its entire row and column are set to 0.
        Uses the first row and first column as markers to optimize space usage.

        Time complexity: O(m * n)
        Space complexity: O(1)
        """

        # Get number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])

        # Flags to check if the first row or first column need to be zeroed
        first_row_zero = False
        first_col_zero = False

        # Check if the first column needs to be zeroed
        for i in range(rows):
            if matrix[i][0] == 0: 
                first_col_zero = True
                break  # No need to check further

        # Check if the first row needs to be zeroed
        for j in range(cols):
            if matrix[0][j] == 0: 
                first_row_zero = True
                break  # No need to check further

        # Use first row and first column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0  # Mark the column for zeroing
                    matrix[i][0] = 0  # Mark the row for zeroing

        # Set entire row to zero based on markers in the first column
        for i in range(1, rows):
            if matrix[i][0] == 0:
                matrix[i] = [0] * cols

        # Set entire column to zero based on markers in the first row
        for j in range(cols):
            if matrix[0][j] == 0:
                for row in range(rows):
                    matrix[row][j] = 0

        # Zero out the first row if it was originally marked
        if first_row_zero:
            matrix[0] = [0] * cols

        # Zero out the first column if it was originally marked
        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0

# Example test case
Solution.setZeroes(Solution, [[1,1,1],[1,0,1],[1,1,1]])
# Expected Output: matrix = [[1,0,1],[0,0,0],[1,0,1]]
