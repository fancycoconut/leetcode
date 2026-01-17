class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedPositionPairs = [ (p,s ) for p, s in zip(position, speed)]
        speedPositionPairs = sorted(speedPositionPairs, reverse=True)
        
        stack = []
        for pos, spd in speedPositionPairs:
            timeToTarget = (target - pos) / spd
            stack.append(timeToTarget)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
