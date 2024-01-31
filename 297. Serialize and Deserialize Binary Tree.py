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
        # preorder traversal and return string
        if not root:
            return "None,"
        return str(root.val) + "," + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # convert string to list
        data = data.split(",")
        # print(data)
        
        def helper(data):
            if data[0] == "None":
                data.pop(0)
                return None
            root = TreeNode(data[0])
            data.pop(0)
            root.left = helper(data)
            root.right = helper(data)
            return root
        
        return helper(data)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))