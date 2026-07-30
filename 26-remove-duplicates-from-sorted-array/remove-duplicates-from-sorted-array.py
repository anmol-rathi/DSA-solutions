class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        h={}
        count=0
        for i in range(len(nums)):
            if nums[i] in h:
                nums[i]=101
                count+=1
            else:
                h[nums[i]]=i
        
        nums.sort()
        
        # print(nums)
        # print(count)
        return len(h)
        