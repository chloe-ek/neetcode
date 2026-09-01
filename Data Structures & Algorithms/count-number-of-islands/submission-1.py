class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        total_island = 0
        visited = set()

        def dfs(r, c):
            # base case 1 : check the range 
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # base case 2 : is this water?
            if grid[r][c] == '0':
                return
            # base case 3 : already visited?
            if (r, c) in visited:
                return
            
            # after passing the base case, it will be island 
            visited.add((r, c))

            # check neighbours => top, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    total_island += 1
                    dfs(row, col)

        return total_island
        
        