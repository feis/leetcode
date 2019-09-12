# 938. Range Sum of BST
# divide-and-conque with pruning
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None:
            return 0
        return ((self.rangeSumBST(root.left, L, R) if L <= root.val else 0)
                + (self.rangeSumBST(root.right, L, R) if root.val <= R else 0)
                + (root.val if L <= root.val <= R else 0))

