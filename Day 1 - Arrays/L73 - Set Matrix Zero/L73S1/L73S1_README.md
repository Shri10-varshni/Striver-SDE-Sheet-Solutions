# Notes for Set Matrix Zeroes - 1

## Approach  
Use two auxiliary arrays (`row_mat` and `col_mat`) to track which rows and columns need to be set to zero, then update the matrix accordingly.  

## Steps  
1. **Initialize Tracking Arrays:**  
   - Create `row_mat` and `col_mat`, initialized with `-1`.  
2. **First Pass (Mark Rows & Columns):**  
   - Traverse the matrix and mark the corresponding row and column in `row_mat` and `col_mat` when a zero is encountered.  
3. **Second Pass (Update Rows):**  
   - Set entire rows to zero if marked in `row_mat`.  
4. **Third Pass (Update Columns):**  
   - Set entire columns to zero if marked in `col_mat`.  

## Edge Cases  
- No zeroes in the matrix (no changes needed).  
- A matrix with all zeroes (entire matrix remains zero).  
- Single row or column matrix.  

## Time Complexity  
- **O(m × n)** – Each cell is visited a constant number of times.  

## Space Complexity  
- **O(m + n)** – Uses additional arrays to track row and column zeroes.  

## Implementation Notes  
- This solution uses extra space (`O(m + n)`) for tracking arrays, whereas an optimized version could modify the matrix in-place using the first row and column.  
