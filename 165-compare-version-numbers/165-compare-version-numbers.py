class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        '''
        version number = joined by .
        
        '''
        version1 = [int(i) for i in version1.split('.')]
        version2 = [int(i) for i in version2.split('.')]
        n1 = len(version1)
        n2 = len(version2)
        
        i = 0
        while i < min(n1,n2):
            if version1[i] > version2[i]:
                return 1
            elif version1[i] < version2[i]:
                return -1
            i+=1
            
        while i < n1:
            if version1[i]!= 0:
                return 1
            i+=1
        
        while i < n2:
            if version2[i]!= 0:
                return -1
            i+=1
        
        return 0