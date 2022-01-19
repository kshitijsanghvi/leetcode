class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        sequence = nums
        n = len(sequence)
        @lru_cache(None)
        def helper(i,prev,state):
            if i == n - 1:
                if sequence[i] > prev:
                    return True
                else:
                    if state == True:
                        return True
                    else:
                        return False

            if sequence[i] <= prev:
                if state == False:
                    return False
                else:
                    return helper(i+1,prev,False)
            else:
                if state== True:
                    return helper(i+1,prev,False) or helper(i+1,sequence[i],True)
                else:
                    return helper(i+1,sequence[i],False)

        return helper(0,float('-inf'),True)  