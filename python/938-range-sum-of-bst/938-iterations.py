# 938. Range Sum of BST
# iteration 
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = [root]
        ans = 0
        while len(stack) > 0:
            root = stack.pop()
            if root == None:
                continue
            stack.append(root.left)
            stack.append(root.right)
            ans += root.val if L <= root.val <= R else 0
        return ans

