class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        r = 0
        l = 0
        while r < len(popped) and l < len(popped):
            while r <len(popped) and l >= 0 and l < len(pushed) and popped[r] == pushed[l]:
                pushed.pop(l)
                l -= 1
                r += 1
            l += 1
            
        return r == len(popped)
            
            