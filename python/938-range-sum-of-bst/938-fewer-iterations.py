# 938. Range Sum of BST
# fewer iteartions
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = [root]
        ans = 0
        while (len(stack) > 0):
            root = stack.pop()
            if root == None:
                continue
            if L <= root.val:
                stack.append(root.left)
            if root.val <= R:
                stack.append(root.right) 
            ans += root.val if L <= root.val <= R else 0
        return ans

