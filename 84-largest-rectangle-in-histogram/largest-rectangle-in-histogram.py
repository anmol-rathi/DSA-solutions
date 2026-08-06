class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # Previous Smaller Element (PSE)
        pse = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)

        # Next Smaller Element (NSE)
        nse = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        output = 0

        for i in range(n):
            width = nse[i] - pse[i] - 1
            output = max(output, heights[i] * width)

        return output

        # class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         res = [-1] * n
#         stack = []
#         for i in range(n):
#             while stack and heights[stack[-1]] >= heights[i]:
#                 stack.pop()
#             if stack:
#                 res[i] = stack[-1]
#             stack.append(i)
        
#         nse = [n] * n
#         stack = []
#         for i in range(n - 1, -1, -1):
#             while stack and heights[stack[-1]] > heights[i]:
#                 stack.pop()
#             if stack:
#                 nse[i] = stack[-1]
#             stack.append(i)
#         output=0
#         for i in range(n):
#             if res[i]==-1 and nse[i]==n:
#                 output=max(heights[i],output)
#             elif res[i]==-1:
#                 output=max(output,heights[i]*(nse[i]-1))
#             else:
#                 output=max(output,heights[i]*(nse[i]-res[i]-1))  
        
#         return output