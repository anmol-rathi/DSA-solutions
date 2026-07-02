class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        output=0
        for i in range(len(tickets)):
            if i<=k:
                output+=min(tickets[i],tickets[k])
            else:
                output+=min(tickets[i],tickets[k]-1)  
        return output      