class Solution:
    def trap(self, height: List[int]) -> int:
        lmax,rmax,total=0,0,0
        l=0
        r=len(height)-1
        while l<r:
            if height[l]<=height[r]:
                if height[l]<lmax:
                    total+=lmax-height[l]
                else:
                    lmax=height[l]
                l+=1
            else:
                if height[r]<rmax:
                    total+=rmax-height[r]
                else:
                    rmax=height[r]
                r-=1
        # print(total)
        return total

            


                
        