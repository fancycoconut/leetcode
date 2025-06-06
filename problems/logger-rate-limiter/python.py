class Logger:

    def __init__(self):
       self.uniqueMessages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.uniqueMessages:
            if timestamp < self.uniqueMessages[message] + 10:
                return False

        self.uniqueMessages[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)