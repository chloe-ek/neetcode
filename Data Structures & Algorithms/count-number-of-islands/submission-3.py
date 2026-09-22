class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        total = 0
        # save (r, c) once visited

        visited = set()

        def dfs(row, col):
            # check the range
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            
            # check if it's water
            if grid[row][col] == '0':
                return 

            # check if it's visited already
            if (row, col) in visited:
                return

            # Add visited
            visited.add((row, col))

            # Check neighbours 
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                dfs(row + dr, col + dc)

        

        # check if it was first time to find the island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    total += 1
                    dfs(r, c)

        return total

