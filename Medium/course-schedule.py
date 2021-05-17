#  https://leetcode.com/problems/course-schedule/
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_mx = {i: [] for i in range(numCourses)}
        for pair in prerequisites:
            adj_mx[pair[0]].append(pair[1])

        visited = set()

        def dfs(node):
            if node in visited:
                return False
            if len(adj_mx[node]) == 0:
                return True

            visited.add(node)
            for pre_node in adj_mx[node]:
                if not dfs(pre_node):
                    return False
            visited.remove(node)
            adj_mx[node] = []
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True

#####################################################################

sln = Solution()
res = sln.canFinish(5, [[1,4],[2,4],[3,1],[3,2]])
print(res)