class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) > 0 and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if len(stack) > 0:
                output[i] = stack[-1] - i

            stack.append(i)
        #print(output)

        return output
