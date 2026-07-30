class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

        return count <= 1

        # n=len(nums)
        # for i in range(n):
        #     print(i)
        #     if 0 < i < len(nums) - 1:
        #         if nums[i]<nums[i-1] and nums[i]<nums[i+1] and nums[i+1]>nums[i-1]:
        #             print(1)
        #             return False
                    
        #     if i < len(nums) - 1:
        #         if nums[i]<=nums[n-1] and nums[i]<nums[i+1] and nums[i+1]>nums[n-1]:
        #             print('hi')
        #             return False

        #     if 0 < i :
        #         if nums[i]<nums[i-1] and nums[i]<nums[0] and nums[0]>nums[i-1]:
        #             print(2)
        #             return False
        # return True
        