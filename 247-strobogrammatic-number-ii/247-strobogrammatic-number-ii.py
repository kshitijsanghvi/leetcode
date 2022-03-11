class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        
        results =[]
        new_results = []
        
        if n % 2 == 1:
            results = ["0","1","8"]
            n = n - 1
        
        while n != 0:
            if not results:
                new_results = ["11","88","69","96"]
                if n > 2:
                    new_results.append("00")
            else:
                for r in results:
                    new_results.append("1"+r+"1")
                    new_results.append("8"+r+"8")                    
                    new_results.append("6"+r+"9")        
                    new_results.append("9"+r+"6")
                    if n > 2:
                        new_results.append("0"+r+"0")
            n = n - 2
            results = new_results
            new_results = []
        
        return results