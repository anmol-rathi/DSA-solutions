class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=sorted(nums)
        res=[]
        dc={}
        for i,val in enumerate(temp):
            if val not in dc:
                dc[val]=i
        for i in nums:
            res.append(dc[i])
        return res

