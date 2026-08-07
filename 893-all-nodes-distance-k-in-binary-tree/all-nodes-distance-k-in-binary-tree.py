# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        stack=[root]
        parent={root:None}
        while stack:
            node=stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left]=node
            if node.right:
                stack.append(node.right)
                parent[node.right]=node
        
        visited=set()
        queue=deque([target])
            
        visited.add(target.val)
        while k!=0:
            for i in range(len(queue)):
                node=queue.popleft()
                if node.left and node.left.val not in visited:
                    queue.append(node.left)
                    visited.add(node.left.val)
                if node.right and node.right.val not in visited:
                    queue.append(node.right)
                    visited.add(node.right.val)
                if parent[node] and parent[node].val not in visited:
                    queue.append(parent[node])
                    visited.add(parent[node].val)
                # print(visited)
            k-=1
        # print(visited)
        # stack=set()
        for i in range(len(queue)):
            print(queue[i].val)
            stack.append(queue[i].val)
        return stack



        # if target.left:
        #     stack.append(target.left)
        #     # visited.add(target.left.val)
        # if target.right:
        #     stack.append(target.right)
        #     # visited.add(target.right.val)
        # if parent[target]:
        #     stack.append(parent[target])
        #     # visited.add(parent[target].val)
        
            




            


        
        
            
        

        