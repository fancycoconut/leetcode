class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:        
        accessMap = {}
        for accessTime in access_times:
            employee = accessTime[0]
            employeeAccesses = accessMap.get(employee, [])
            employeeAccesses.append(accessTime[1])
            accessMap[employee] = employeeAccesses
        #print(accessMap)
        
        output = []
        for employee in accessMap.keys():
            accessTimes = sorted(accessMap[employee])

            for i in range(len(accessTimes) - 2):
                end = int(accessTimes[i + 2])
                start = int(accessTimes[i])
                if end - start < 100:
                    output.append(employee)
                    break

        return output