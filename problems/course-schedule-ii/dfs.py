class Solution:
    # This is basically topological sort
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = { course:[] for course in range(numCourses) }
        for course,prereq in prerequisites:
            courseMap[course].append(prereq)
        print(courseMap)

        output = []
        uniqueOutput = set()
        visited = set()
        def dfs(course) -> bool:
            if course in visited:
                return False
            deps = courseMap[course]
            if len(deps) == []:
                return True
            
            visited.add(course)
            for dep in deps:
                if not dfs(dep):
                    return False
            
            visited.remove(course)
            courseMap[course] = []

            if course not in uniqueOutput:
                output.append(course)
                uniqueOutput.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return output
