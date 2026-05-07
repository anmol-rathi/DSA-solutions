class Solution:
    def climbStairs(self, n: int) -> int:
        a=[1,2]
        arr=[0]*(n+1)
        arr[0]=1
        for i in range(1,len(arr)):
            for j in a:
                if (i-j)>=0:
                    arr[i]+=arr[i-j]
        return arr[n]  