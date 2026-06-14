"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        nodes = []
        for i in range(100):
            nodes.append(Node(i+1))

        def bfs(node):
            q = deque()
            q.append(node)
            v = set()
            while q:
                curr = q.popleft()
                v.add(curr.val)
                for n in curr.neighbors:
                    if n.val not in v:
                        q.append(n)
                        nodes[curr.val-1].neighbors.append(nodes[n.val-1])
                        nodes[n.val-1].neighbors.append(nodes[curr.val-1])

    
        bfs(node)
        
        return nodes[0]

             

            


        