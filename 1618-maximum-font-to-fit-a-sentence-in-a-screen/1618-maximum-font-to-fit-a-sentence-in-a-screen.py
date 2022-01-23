# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        def compute_width(f):
            return sum( [fontInfo.getWidth(f,c) for c in text] )
        
        if fontInfo.getHeight(fonts[0]) > h or compute_width(fonts[0]) > w:
            return -1
        
       
        l = 0
        r = len(fonts) - 1
        
        # Find max font - height
        
        while l < r-1:
            mid = l + (r-l)//2
            
            if h >= fontInfo.getHeight(fonts[mid]):
                l = mid
            else:
                r = mid - 1
        
        if h >= fontInfo.getHeight(fonts[r]):
            idx = r
        else:
            idx = l
            
        # Find max width
        
        l = 0
        r = idx
        
        while l < r - 1:
            mid = l + (r-l)//2
            if w >= compute_width(fonts[mid]):
                l = mid
            else:
                r = mid - 1
        
        if w >= compute_width(fonts[r]):
            return fonts[r]
        else:
            return fonts[l]
                
            
        
            
        
        
        
        
        
        
        
        
        