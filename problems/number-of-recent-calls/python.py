# Brute force approach
class RecentCounter:

    def __init__(self):
        self.requests = []
        self.start = 0
        self.end = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.start = t - 3000
        self.end = t

        output = 0
        for r in self.requests:
            if r >= self.start and r <= self.end:
                output += 1
        return output


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)