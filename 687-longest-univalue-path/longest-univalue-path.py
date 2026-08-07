# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        parent={root:None}
        stack=[root]
        while stack:
            node=stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left]=node
            if node.right:
                stack.append(node.right)
                parent[node.right]=node
        m=0
        for i in parent:
            stack=[(i,1)]
            s=set()
            max_count=0
            while stack:
                node,count=stack.pop()
                if node in s: 
                    continue
                else:
                    s.add(node)
                max_count = max(max_count, count)
                if node.left and node.val==node.left.val and node.left not in s:
                    stack.append((node.left,count+1))

                if node.right and node.val==node.right.val and node.right not in s:
                    stack.append((node.right,count+1))

                if parent[node] and node.val==parent[node].val and parent[node] not in s:
                    stack.append((parent[node],count+1))
            max_count -= 1
            m = max(m, max_count)
        # print(m)
        return m
            
        




            

        