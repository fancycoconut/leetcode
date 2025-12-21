class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        sortedAccessTimes = sorted(access_times, key=lambda tup:tup[1])
        
        accessMap = {}
        for accessTime in sortedAccessTimes:
            employee = accessTime[0]
            employeeAccesses = accessMap.get(employee, [])
            employeeAccesses.append(accessTime[1])
            accessMap[employee] = employeeAccesses
        #print(accessMap)
        
        output = []
        for employee in accessMap.keys():
            accessTimes = accessMap[employee]

            for i in range(len(accessTimes) - 1, -1, -1):
                end = int(accessTimes[i])
                count = 1

                for j in range(i - 1, -1, -1):
                    start = int(accessTimes[j])

                    if end - start < 100:
                        count += 1

                if count >= 3:
                    output.append(employee)
                    break
                

        return output
