# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.d = {}
        self.c = -1
        q = [root]
        while q:
            cn = q.pop(0)
            self.c+=1
            self.d[self.c] = cn
            if cn.left:
                q.append(cn.left)
            if cn.right:
                q.append(cn.right)
                
                
    def insert(self, val: int) -> int:
        self.c += 1
        self.d[self.c] =TreeNode(val)
        p = (self.c - 1)//2
        if p *2 + 1 == self.c:
            self.d[p].left = self.d[self.c]
        else:
            self.d[p].right = self.d[self.c]
        return self.d[p].val
    def get_root(self) -> Optional[TreeNode]:
        return self.d[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()