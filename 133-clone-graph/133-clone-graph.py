"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        v = {}
        v_copy = {}
        q = [node]
        v[node.val] = 1
        clone = Node()
        clone.val = node.val
        v_copy[clone.val] = clone
        while q:
            cn = q.pop()
            # print(cn.val)    
            for nn in cn.neighbors:
                if nn.val not in v:
                    v[nn.val] = nn
                    v_copy[nn.val] = Node()
                    v_copy[nn.val].val = nn.val
                    q.append(nn)
                v_copy[cn.val].neighbors.append(v_copy[nn.val])
                
        return clone
        