class FileSystem:

    def __init__(self):
        self.d = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.d:
            return False
        
        idx = path.rindex('/')
        
        if idx == 0:
            self.d[path] = value
            return True
        else:
            p1 = path[:idx]
            if p1 in self.d:
                self.d[path] = value
                return True
            else:
                return False

    def get(self, path: str) -> int:
        if path in self.d:
            return self.d[path]
        else:
            return -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)