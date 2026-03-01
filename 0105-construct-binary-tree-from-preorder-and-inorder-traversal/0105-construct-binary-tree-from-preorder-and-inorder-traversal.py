class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {}
        for i, v in enumerate(inorder):
            idx[v] = i
        pre_i = 0
        def build_subtree(inL: int, inR: int) -> Optional[TreeNode]:
            nonlocal pre_i # allow build_subtree() to advance outer preorder pointer (pre_i += 1)
            if inL > inR: 
                return None
            root_val = preorder[pre_i]
            pre_i += 1

            mid = idx[root_val]
            root = TreeNode(root_val)
            root.left = build_subtree(inL, mid-1)
            root.right = build_subtree(mid+1, inR)
            return root

        return build_subtree(0, len(inorder) - 1)