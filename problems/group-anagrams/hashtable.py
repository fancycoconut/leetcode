class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        groups = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]

        output = []
        for k,v in groups.items():
            output.append(v)
        return output