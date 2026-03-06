class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node:
                res.append("None")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None

        vals = data.split(",")
        i = 0
        def build():
            nonlocal i
            if vals[i] == "None":
                i += 1
                return None
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = build()
            node.right = build()
            return node            
        return build()