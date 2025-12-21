class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majorityAmount = len(nums) // 3
        
        output = set()
        elementMap = {}
        for num in nums:
            count = elementMap.get(num, 0)
            count += 1
            elementMap[num] = count
        
            if count > majorityAmount:
                output.add(num)
        #print(output)
        
        return list(output)
