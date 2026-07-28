class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        a=list(s)
        b=list(goal)
        for i in range(len(s)):
            if a==b:
                return True
            c=a.pop(0)
            a.append(c)
        return False 
        # print(a.pop(0))
        # print(a)

            
        