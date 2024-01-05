class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, diameter = self.height_and_diameter(root)
        return diameter

    def height_and_diameter(self, root):
        if root is None:
            return 0, 0

        left_height, left_diameter = self.height_and_diameter(root.left)
        right_height, right_diameter = self.height_and_diameter(root.right)

        current_height = 1 + max(left_height, right_height)
        height_diameter = left_height + right_height
        current_diameter = max(height_diameter, left_diameter, right_diameter)

        return current_height, current_diameter