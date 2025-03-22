from typing import Counter

from collections import Counter

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = [tuple(row) for row in grid]          # Convert rows into tuples
        columns = [tuple(col) for col in zip(*grid)] # Convert columns into tuples
        
        row_counts = Counter(rows)   # Count occurrences of each row
        col_counts = Counter(columns) # Count occurrences of each column

        count = 0
        for row in row_counts:
            if row in col_counts:
                count += row_counts[row] * col_counts[row]  # Multiply occurrences
        
        return count


     

test = Solution()
test.equalPairs([
    [3, 1, 2, 2], 
    [1, 4, 4, 5], 
    [2, 4, 2, 2], 
    [2, 4, 2, 2]
])