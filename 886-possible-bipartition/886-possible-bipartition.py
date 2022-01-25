class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        d = [sorted(i) for i in dislikes]
        
        d1 = {}
        d2 = {}
        
        prev = 0
        
        while d:
            ud = []
            if prev == len(d):
                i = d[0]
                if i[0] in d1:
                    d2[i[1]] = 1


                elif i[0] in d2:
                    d1[i[1]] = 1


                elif i[1] in d1:
                    d2[i[0]] = 1


                elif i[1] in d2:
                    d1[i[0]] = 1
                else:
                    d1[i[0]] = 1
                    d2[i[1]] = 1

                d= d[1:]

            for i in d:
                if i[0] in d1 and i[1] in d1:
                    return False

                if i[0] in d2 and i[1] in d2:
                    return False

                if i[0] in d1:
                    d2[i[1]] = 1
                    continue

                if i[0] in d2:
                    d1[i[1]] = 1
                    continue

                if i[1] in d1:
                    d2[i[0]] = 1
                    continue

                if i[1] in d2:
                    d1[i[0]] = 1
                    continue
                
                ud.append(i)
            
            prev = len(d)
            d = ud
            
        return True