class HitCounter:

    def __init__(self):
        self.timestamps = []

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)
        #print(self.timestamps)

    def getHits(self, timestamp: int) -> int:
        hits = 0
        i = len(self.timestamps) - 1

        while i >= 0 and self.timestamps[i] > timestamp - 300:
            hits += 1
            i -= 1
            
        return hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
