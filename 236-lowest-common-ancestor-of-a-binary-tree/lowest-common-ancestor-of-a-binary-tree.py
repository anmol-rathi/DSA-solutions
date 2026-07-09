# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue=deque([root])
        parent={root:None}
        while queue:
            node=queue.popleft()
            if node.left:
                queue.append(node.left)
                parent[node.left]=node
            if node.right:
                queue.append(node.right)
                parent[node.right]=node
            if p in parent and q in parent:
                break
        p1,p2=p,q
        while p1!=p2:
            p1=parent[p1] if p1 else q
            p2=parent[p2] if p2 else p
        return p1
        