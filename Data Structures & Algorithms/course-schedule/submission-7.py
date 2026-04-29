class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i : [] for i in range(numCourses)}

        for course, pre in prerequisites:
            adjMap[course].append(pre)

        visiting = set()
        visited = set()

        def dfs(c):
            if c in visited:
                return True
            if c in visiting:
                return False

            visiting.add(c)
            for neighbor in adjMap[c]:
                if not dfs(neighbor):
                    return False

            visiting.remove(c)
            visited.add(c)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True

        