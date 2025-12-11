class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for num in nums:
            count = numMap.get(num, 0)
            numMap[num] = count + 1
        #print(numMap)

        output = []

        answer = set()
        for i in range(k):
            num = 0
            numOfElements = 0
            for k,v in numMap.items():
                if k in answer:
                    continue
                if v > numOfElements:
                    numOfElements = v
                    num = k
            output.append(num)
            answer.add(num)    

        return output
