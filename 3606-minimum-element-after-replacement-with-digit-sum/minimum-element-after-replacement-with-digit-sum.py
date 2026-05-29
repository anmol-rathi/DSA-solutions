class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]
        for i,val in enumerate(nums):
            s=0
            while(val!=0):
                val,r=divmod(val,10)
                s+=r
            arr.append(s)
        return min(arr)
                
                    