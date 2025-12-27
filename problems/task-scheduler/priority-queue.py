class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = Counter(tasks)
        maxHeap = [ -count for count in taskMap.values() ]
        heapq.heapify(maxHeap)
        
        time = 0
        queue = deque()
        while len(queue) > 0 or len(maxHeap) > 0:
            time += 1

            if len(maxHeap) > 0:
                taskCount = abs(heapq.heappop(maxHeap)) - 1
                if taskCount > 0:
                    queue.append((taskCount, time + n))
            
            if len(queue) > 0 and queue[0][1] == time:
                task = queue.popleft()
                heapq.heappush(maxHeap, -task[0])

        return time
