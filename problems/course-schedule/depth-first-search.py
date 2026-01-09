class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list
        dependencyMap = { }
        for item in prerequisites:
            course, prereq = item[0], item[1]
            dependencies = dependencyMap.get(course, [])
            dependencies.append(prereq)
            dependencyMap[course] = dependencies
        #print(dependencyMap)
        
        # Check for cycle
        visited = set()
        def dfs(course) -> bool:
            if course in visited:
                return False
            dependencies = dependencyMap.get(course, [])
            if len(dependencies) == 0:
                return True

            visited.add(course)
            for dep in dependencies:
                if not dfs(dep):
                    return False

            # Reset / clear dependencies if no cycle is found
            visited.remove(course)
            dependencyMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        