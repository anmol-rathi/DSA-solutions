# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack=[]
        arr=[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                arr.append(root.val)
                root=root.right
        n=len(arr)
        mid=n//2
        root=TreeNode(arr[mid])
        
        queue=deque()
        queue.append((root,0,mid-1))
        queue.append((root,mid+1,n-1))
        while queue:
            node,left,right=queue.popleft()
            if left<=right:
                mid=(left+right)//2
                child=TreeNode(arr[mid])
                if node.val<arr[mid]:
                    node.right=child
                else:
                    node.left=child
                queue.append((child,left,mid-1))
                queue.append((child,mid+1,right))
        return root
        

        