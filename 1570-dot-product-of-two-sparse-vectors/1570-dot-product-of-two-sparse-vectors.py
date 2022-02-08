class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {}
        self.n = len(nums)
        for i in range(len(nums)):
            if nums[i]:
                self.d[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        s = 0
        for i in self.d:
            s += self.d[i] * vec.d[i] if i in vec.d else 0
        return s

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)