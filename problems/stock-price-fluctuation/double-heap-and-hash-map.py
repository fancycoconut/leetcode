class StockPrice:

    def __init__(self):
        self.minPrices = []
        self.maxPrices = []
        self.priceMap = {}
        self.currentTime = 0

    def update(self, timestamp: int, price: int) -> None:
        self.priceMap[timestamp] = price
        heapq.heappush(self.minPrices, (price, timestamp))
        heapq.heappush(self.maxPrices, (-price, timestamp))

        self.currentTime = max(self.currentTime, timestamp)

    def current(self) -> int:
        return self.priceMap[self.currentTime]

    def maximum(self) -> int:
        price, timestamp = self.maxPrices[0]
        while -price != self.priceMap[timestamp]:
            heapq.heappop(self.maxPrices)
            price, timestamp = self.maxPrices[0]
        return -price

    def minimum(self) -> int:
        price, timestamp = self.minPrices[0]
        while price != self.priceMap[timestamp]:
            heapq.heappop(self.minPrices)
            price, timestamp = self.minPrices[0]
        return price
        

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()