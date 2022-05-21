class Solution:
    def countArrangement(self, n: int) -> int:
        temp = []
        seen = [0] * (n+1)
        ans = 0
        def gen_permutation():
            nonlocal temp,seen, ans
            if len(temp) == n:
                ans +=1
            else:
                for i in range(1,n+1):
                    index = len(temp) + 1
                    if seen[i] == 0 and (i % index == 0 or index % i == 0):
                        seen[i] = 1
                        temp.append(i)
                        gen_permutation()
                        temp.pop()
                        seen[i] = 0
        gen_permutation()
        return ans