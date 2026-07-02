class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m= len(grid[0])
        perimeter = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0: continue
                perimeter += 4
                if r>0:
                    perimeter -= grid[r-1][c] 
                if c>0:
                    perimeter -= grid[r][c-1]
                if r<n-1:
                    perimeter -= grid[r+1][c] 
                if c<m-1:
                    perimeter -= grid[r][c+1]
        return perimeter