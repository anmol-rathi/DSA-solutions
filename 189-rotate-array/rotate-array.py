class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b=k%len(nums)
        for i in range(len(nums)-b):
            a=nums.pop(0)
            nums.append(a)
        
        
        