# 938. Range Sum of BST
# divide-and-conque
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None:
            return 0
        return (self.rangeSumBST(root.left, L, R)
                + self.rangeSumBST(root.right, L, R)
                + (root.val if L <= root.val <= R else 0))

