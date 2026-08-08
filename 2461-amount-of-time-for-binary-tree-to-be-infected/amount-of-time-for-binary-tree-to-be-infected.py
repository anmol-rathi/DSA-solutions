# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0
        parent={}
        stack=deque([root])
        parent[root]=None
        target=None
        while stack:
            node=stack.popleft()
            if node.val==start:
                target=node
            if node.left:
                stack.append(node.left)
                parent[node.left]=node
            if node.right:
                stack.append(node.right)
                parent[node.right]=node
        s=set()
        s.add(target)
        stack.append(target)
        count=0
        while len(s)<len(parent):
            for i in range(len(stack)):
                node=stack.popleft()
                # print(node.val)
                # a=len(s)
                if node.left and node.left not in s:
                    stack.append(node.left)
                    s.add(node.left)
                if node.right and node.right not in s:
                    stack.append(node.right)
                    s.add(node.right)
                if parent[node] and parent[node] not in s:
                    stack.append(parent[node])
                    s.add(parent[node])
                # if a==len(s):
                #     continue
            count+=1
            # print(count)
        return count
       

        