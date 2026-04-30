class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        pacific = set()
        atlantic = set()

        def dfs(i, j, visited):
            visited.add((i, j))
            for d in dirs:
                newI = i + d[0]
                newJ = j + d[1]
                if (newI, newJ) not in visited and 0 <= newI < rows and 0 <= newJ < cols and heights[newI][newJ] >= heights[i][j]:
                    dfs(newI, newJ, visited)

        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols - 1, atlantic)

        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows - 1, j, atlantic)

        return [[i, j] for i in range(rows) for j in range(cols) if (i, j) in pacific and (i, j) in atlantic]