class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        ans=[]
        n=len(asteroids)
        for i in asteroids:
            if i>=0:
                stack.append(i)
            else:
                if not stack:
                    ans.append(i)
                while stack:
                    a=stack.pop()
                    if a>(-(i)):
                        stack.append(a)
                        break
                    elif a==-(i):
                        break
                    elif stack:
                        continue
                    else:
                        ans.append(i)
                
        while stack:
            ans.append(stack.pop(0))
        print(ans)
        return ans
            
