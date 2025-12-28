class FileSystem:

    def __init__(self):
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        if not self.isPathValid(path):
            return False
        if path in self.paths:
            return False
        if not self.parentPathExists(path):
            return False

        self.paths[path] = value
        return True

    def parentPathExists(self, path: str) -> bool:
        parts = path.split("/")
        #print(parts)

        p = ""
        for i in range(len(parts) - 1):
            part = parts[i]
            if part == "":
                continue
            
            p += f"/{part}"
            #print(p)
            if p not in self.paths:
                return False

        return True


    def isPathValid(self, path: str) -> bool:
        if len(path) <= 1:
            return False

        if path[0] != "/":
            return False

        return True

    def get(self, path: str) -> int:
        if path not in self.paths:
            return -1

        return self.paths[path]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)