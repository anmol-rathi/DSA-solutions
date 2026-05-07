class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j=0
        res=float('inf')
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            while(total>=target):
                res=min(res,i-j+1)
                total-=nums[j]
                j+=1
        if res<inf:
            return res
        else:
            return 0





        