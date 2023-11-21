# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    #return array which contain the paths possible in a binary tree
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        #if root is null then return empty array
        if root is None:
            return []
        #if root is the leaf node then return the root value
        if root.left is None and root.right is None:
            return [str(root.val)]
        #get the left and right subtree paths
        left_subtree_paths = self.binaryTreePaths(root.left)
        right_subtree_paths = self.binaryTreePaths(root.right)
        #append the root value to the left and right subtree paths
        left_subtree_paths = [str(root.val) + "->" + path for path in left_subtree_paths]
        right_subtree_paths = [str(root.val) + "->" + path for path in right_subtree_paths]
        #return the left and right subtree paths
        return left_subtree_paths + right_subtree_paths

        