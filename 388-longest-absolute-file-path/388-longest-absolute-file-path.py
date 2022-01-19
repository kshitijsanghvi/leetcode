class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input = input.split('\n')
        ml = 0 
        d = defaultdict(int)
        for i in input:
            c = i.count('\t')
            i = i[c:]
            if c == 0:
                d[0] = len(i)
            else:
                d[c] =  d[c-1] + 1 + len(i)
            # print(i,d[c])
            if '.' in i:
                ml = max(ml,d[c])
        return ml