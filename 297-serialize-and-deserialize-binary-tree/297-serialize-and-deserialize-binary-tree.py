# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def dfs(node):
            if not node:
                ans.append("")
                return
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        i = -1
        def dfs_build():
            nonlocal i
            i+=1
            if data[i] != "":
                cn = TreeNode(data[i])
                cn.left = dfs_build() if i + 1 < len(data) else None
                cn.right = dfs_build() if i + 1 < len(data) else None
                return cn
            else:
                return None
            
        return dfs_build()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))