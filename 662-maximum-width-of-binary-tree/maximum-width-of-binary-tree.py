# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=deque([(root,1)])
        res=[]
        while queue:
            level=[]
            for i in range(len(queue)):
                node,num=queue.popleft()
                if node.left:
                    queue.append((node.left,2*num))
                if node.right:
                    queue.append((node.right,(2*num)+1))
                level.append(num)
            res.append(level)
        m=0
        for i in res:
            m=max(m,i[-1]-i[0]+1)
        
        return m



        