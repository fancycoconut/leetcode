class RandomizedSet:
    def __init__(self):
        self.itemMap = {}
        self.items = []

    def insert(self, val: int) -> bool:
        if val in self.itemMap:
            return False

        self.items.append(val)
        self.itemMap[val] = len(self.items) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.itemMap:
            return False

        index = self.itemMap[val]
        temp = self.items[-1]
        self.items[-1] = self.items[index]
        self.items[index] = temp
        self.itemMap[temp] = index

        self.items.pop()
        self.itemMap.pop(val)
        return True

    def getRandom(self) -> int:
        if len(self.items) == 1:
            return self.items[0]

        randomIndex = random.randint(0, len(self.items) - 1)
        return self.items[randomIndex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()