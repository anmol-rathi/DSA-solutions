class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        h={}
        for i in range(len(nums2)-1,-1,-1):
            while stack:
                if stack[-1]>nums2[i]:
                    h[nums2[i]]=stack[-1]
                    stack.append(nums2[i])
                    break
                else:
                    stack.pop()
            if not stack:
                stack.append(nums2[i])
                h[nums2[i]]=-1
        ans=[]
        for i in nums1:
            ans.append(h[i])
        return ans



