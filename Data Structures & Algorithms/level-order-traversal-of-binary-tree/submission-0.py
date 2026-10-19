from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            level_total = len(queue)
            cur = []
            for _ in range(level_total):
                element = queue.popleft()
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
                cur.append(element.val)
            res.append(cur)
        return res