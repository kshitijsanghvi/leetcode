class Solution:
    def minSumOfLengths(self, arr, target):
        '''
        Note: all numbers are positive.
        
        Strategy: Keep a track of minimum length as seen before the starting index of the current subarray with the sum is equal to target
        
        Then a candidate answer becomes: current length + the smallest seen before
        Variable names:
        l : start of new window
        r : end of new window
        Length of window = r - l + 1
        
        We need to keep the previous min at each index in memory because overlap is not allowed
        '''
        
        n = len(arr)
        r = 0
        l = 0
        current_subarray_sum = 0
        ans = float('inf')
        # Size is n + 1 to deal with initial condition
        dp = [float('inf') for i in range(n+1)]
        
        while r < n:
            current_subarray_sum += arr[r]
            
            if current_subarray_sum >= target:
                while current_subarray_sum >= target:
                    if current_subarray_sum == target:
                        current_subarray_length = r - l + 1
                        previous_minimum_subarray_length = dp[l]
                        ans = min(ans, current_subarray_length + previous_minimum_subarray_length)
                        #Updating dp[r] as overlapping solutions are not allowed and it only becomes available when l crosses r
                        dp[r+1] = min(previous_minimum_subarray_length,current_subarray_length)
                    dp[l+1] = min(dp[l+1],dp[l])
                    current_subarray_sum -= arr[l]
                    l+=1
            r+=1
        return ans if ans != float('inf') else -1
        
        