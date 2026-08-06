# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack=[(root,0,0)]
        h={}
        while stack:
            node,row,col=stack.pop()
            if col in h:
                h[col].append([row,node.val])
            else:
                h[col]=[[row,node.val]]
            if node.right:
                stack.append((node.right,row+1,col+1))
            if node.left:
                stack.append((node.left,row+1,col-1))
        
        ans=[]
        for key in sorted(h):
            h[key].sort()
            temp=[]
            for row,val in h[key]:
                temp.append(val)
            ans.append(temp)  
        # print(ans)
        return ans


        