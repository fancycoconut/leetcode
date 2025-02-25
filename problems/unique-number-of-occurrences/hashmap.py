class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for num in arr:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        uniqueOccurences = set()
        for key, value in map.items():
            if value in uniqueOccurences:
                return False
            uniqueOccurences.add(value)

        return True
        