class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr=[]
        for i in range(len(nums)):
            if nums[i]==0:
                arr.append(i)
        # print(arr)
        count=0
        for i in range(len(arr)):
            nums.append(nums.pop(arr[i]-count))
            count+=1


        