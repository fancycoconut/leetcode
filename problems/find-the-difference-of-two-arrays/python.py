class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diffa = set()
        diffb = set()
        seta = set()
        setb = set()
        for a in nums1:
            seta.add(a)
        
        for b in nums2:
            setb.add(b)

        for a in nums1:
            if a in setb:
                continue
            diffa.add(a)

        for b in nums2:
            if b in seta:
                continue
            diffb.add(b)

        return [ list(diffa), list(diffb) ]
        
        