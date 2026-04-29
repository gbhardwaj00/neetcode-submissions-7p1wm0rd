"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = deque([root])
        while q:
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    node.next = q[0] if i < qLen - 1 else None
                    q.append(node.left)
                    q.append(node.right)

        return root