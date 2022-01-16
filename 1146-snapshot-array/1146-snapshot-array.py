class SnapshotArray:

    def __init__(self, length: int):
        self.d = {i:[[-1,0]] for i in range(length)}
        self.s = -1
    def set(self, index: int, val: int) -> None:
        self.d[index].append([self.s,val])
        

    def snap(self) -> int:
        self.s+=1
        return self.s

    def get(self, index: int, snap_id: int) -> int:
        l = self.d[index]
        i = bisect.bisect_right(l,[snap_id])-1
        return l[i][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)