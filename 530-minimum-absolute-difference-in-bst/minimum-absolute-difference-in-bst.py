# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack=[]
        min_diff=float("inf")
        prev=float("-inf")
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                min_diff=min(min_diff,root.val-prev)
                prev=root.val
                root=root.right
        
        return min_diff



        # if not root or (not root.left and not root.right):
        #     return 0
        # min_diff=float("inf")
        # stack=[(root,min_diff)]
        
        # while stack:
        #     node,parent=stack.pop()
        #     diff=parent-node.val
        #     if diff<0:
        #         diff=diff*(-1)
        #     min_diff=min(min_diff,diff)
        #     if node.left:
        #         stack.append((node.left,node.val))
        #     if node.right:
        #         stack.append((node.right,node.val))
        
        # return min_diff


        
        