class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in map.keys():
                map[num].append(i)
            else:
                map[num] = [ i ]

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in map.keys():
                if len(map[diff]) == 2:
                    return map[diff]

                if i == map[diff][0]:
                    continue
                else:
                    return [ i, map[diff][0] ]
        
        return []