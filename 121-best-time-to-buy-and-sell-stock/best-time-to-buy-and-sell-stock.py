class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t=0
        p=1
        maxp=0
        while p!=len(prices):
            if prices[t]<prices[p]:
                res=prices[p]-prices[t]
                maxp=max(maxp,res)
            else:
                t=p
            p+=1
        return maxp
            
            
        