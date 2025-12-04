class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numMap = {}
        for i,num in enumerate(numbers):
            if num in numMap:
                numMap[num].append(i)
            else:
                numMap[num] = [i]
        
        output = []
        for i,num in enumerate(numbers):
            complement = target - num
            if complement in numMap:
                output.append(i + 1)
                
                secondIndex = i
                while secondIndex == i:
                    secondIndex = numMap[complement].pop(0)
                output.append(secondIndex + 1)
                break
                
        return output