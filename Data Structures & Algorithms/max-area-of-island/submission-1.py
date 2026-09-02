class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0
        visited = set()

        def dfs(r, c):
            area = 0
            # out of range
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if (r, c) in visited:
                return 0
            if grid[r][c] == 0:
                return 0

            visited.add((r, c))
            area = 1

            direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in direction:
                area += dfs(r + dr, c + dc)

            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:

                    max_area = max(max_area, dfs(row, col))


        return max_area
                    





        
        