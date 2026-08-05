class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[-inf]*(len(nums))
        for i in range(len(nums)-1,-1,-1):
            while stack:
                if stack[-1]>nums[i]:
                    res[i]=stack[-1]
                    stack.append(nums[i])
                    break
                else:
                    stack.pop()
            if not stack:
                stack.append(nums[i])

        print(res)
        print(stack)
        for i in range(len(nums)-1,-1,-1):
            
            if res[i]!=-inf:
                continue
            while stack:
                if stack[-1]>nums[i]:
                    res[i]=stack[-1]
                    break
                elif stack[0]==nums[i]:
                    res[i]=-1
                    break
                else:
                    stack.pop()
        
        return res
            

            
        