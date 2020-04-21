class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # check if empty
        if not grid:
            return 0

        count = 0
        # len(grid) number of the rows
        # len(grid[0]) number of the columns
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count +=1
        return count


    def dfs(self, grid, i, j):
        if ( i < 0 or j < 0 or
            i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1' ) :
            return
        else:
            #mark as visited
            grid[i][j] = '#'
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)
