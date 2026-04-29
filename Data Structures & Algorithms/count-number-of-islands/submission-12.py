class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0

        def visit(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "0" or (i, j) in visited:
                return
            visited.add((i, j))
            visit(i + 1, j)
            visit(i, j + 1)
            visit(i - 1, j)
            visit(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    res += 1
                    visit(i, j)

        return res

        

                    