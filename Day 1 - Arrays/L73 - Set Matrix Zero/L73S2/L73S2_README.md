# Notes for Set Matrix Zeroes - 2

## Approach  
Optimize space usage by using the first row and first column as markers instead of additional arrays.  

## Steps  
1. **Check First Row & Column:**  
   - Determine if the first row or first column should be zeroed.  
2. **Mark Rows & Columns:**  
   - Traverse the matrix (excluding first row & column) and mark zeroes in the first row/column as indicators.  
3. **Update Matrix Using Markers:**  
   - Zero out rows and columns based on markers.  
4. **Handle First Row & Column:**  
   - If initially marked, set them to zero.  

## Edge Cases  
- No zeroes in the matrix (no changes needed).  
- A matrix with all zeroes (remains zero).  
- Single row or single column matrix.  

## Time Complexity  
- **O(m × n)** – Each cell is processed a constant number of times.  

## Space Complexity  
- **O(1)** – No extra space used, modifications are done in-place.  

## Implementation Notes  
- The first row/column is used for marking, so modifications should be done carefully to avoid overwriting data prematurely.  
