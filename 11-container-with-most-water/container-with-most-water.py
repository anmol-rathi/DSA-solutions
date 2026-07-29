class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxw=0
        n=len(height)
        l=0
        r=len(height)-1
        while(l<r):
            maxw=max(maxw,min(height[l],height[r])*(r-l))
            if height[r]>height[l]:
                l+=1
                
            else:
                r-=1
                
            
        return maxw
                
            
        return maxw

        