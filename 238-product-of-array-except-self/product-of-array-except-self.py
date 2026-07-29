class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[1]*(len(nums))
        b=[1]*(len(nums))
        n=len(nums)
        for i in range(1,n):
            if i==1:
                a[i]=nums[i-1]
                b[n-i-1]=nums[n-1]
            else:
                a[i]=a[i-1]*nums[i-1]
                b[n-i-1]=b[n-i]*nums[n-i]
        # print(a)
        # print(b)
        for i in range(n):
            a[i]=a[i]*b[i]
        
        return a
        