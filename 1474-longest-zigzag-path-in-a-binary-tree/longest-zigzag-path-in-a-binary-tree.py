# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        r=1
        l=0
        stack=[]
        if root.left:
            stack.append((root.left,0,1))
        if root.right:
            stack.append((root.right,1,1))
        m=0
        while stack:
            node,d,count=stack.pop()
            m=max(m,count)
            if d==l:
                if node.left:
                    stack.append((node.left,l,1))
                if node.right:
                    stack.append((node.right,r,count+1))
            if d==r:
                if node.left:
                    stack.append((node.left,l,count+1))
                if node.right:
                    stack.append((node.right,r,1))
        return m
                    

        