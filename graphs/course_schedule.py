'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)} #dic node: []

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre) #dic node: [pre1, pren]

        visiting = set()

        def dfs(crs):
            if crs in visiting: # cycle
                return False
            if preMap[crs] == []: # no prereq
                return True

            visiting.add(crs) # couse with prereq
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            visiting.remove(crs) # 
            preMap[crs] = []
            return True

        for c in range(numCourses): 
            if not dfs(c): # acyclic must return True
                return False
        return True
    

numCourses = 7
prerequisites = [[1,0], [0,3], [0,2], [3,2], [2,5], [4,5], [5,6], [2,4]] # True, we have to figure out if it is acyclic
print(Solution().canFinish(numCourses, prerequisites))