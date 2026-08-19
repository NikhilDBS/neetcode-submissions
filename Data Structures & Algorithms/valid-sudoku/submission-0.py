from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create a dictionary to store list of (row, col) coordinates for digits '1'..'9'
        digit_positions = defaultdict(list)
        
        # Step 1: Collect coordinates for each digit
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    digit_positions[val].append((r, c))
                    
        # Step 2: Check row, column, and 3x3 box collisions for each digit
        for digit, positions in digit_positions.items():
            rows = set()
            cols = set()
            boxes = set()
            
            for r, c in positions:
                # Calculate 3x3 box coordinates as a tuple (0 to 2, 0 to 2)
                box_id = (r // 3, c // 3)
                
                # If row, col, or box index has already been seen for this digit
                if r in rows or c in cols or box_id in boxes:
                    return False
                
                rows.add(r)
                cols.add(c)
                boxes.add(box_id)
                
        return True