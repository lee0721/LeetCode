class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_i = 0

        for v in preorder[1:]: # start from preorder[1]
            node = stack[-1]
            if node.val != inorder[inorder_i]:
                node.left = TreeNode(v)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorder_i]:
                    node = stack.pop()
                    inorder_i += 1
                node.right = TreeNode(v)
                stack.append(node.right)
        return root