class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        # a=0
        # alice=0
        # bob=0
        # count=0
        # while piles:
        #     a=0
        #     if piles[0]>piles[len(piles)-1]:
        #         a+=piles[0]
        #         piles.pop(0)
        #     elif piles[0]<piles[len(piles)-1]:
        #         a+=piles[len(piles)-1]
        #         piles.pop()
        #     else:
        #         i=1
        #         j=len(piles)-2
        #         while i<=j:
                    
        #             if piles[i]<piles[j]:
        #                 a+=piles[0]
        #                 piles.pop(0)
        #                 break
        #             elif piles[i]>piles[j]:
        #                 a+=piles[len(piles)-1]
        #                 piles.pop()
        #                 break
        #             else:
        #                 i+=1
        #                 j-=1
        #         else:
    
        #             a += piles[0]
        #             piles.pop(0)
        #     if count%2==0:
        #         alice+=a
        #     else:
        #         bob+=a
        #     count+=1
        # if alice>bob:
        #     return True
        # else:
        #     return False




        