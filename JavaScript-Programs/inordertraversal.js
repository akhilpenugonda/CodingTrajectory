var inorderTraversal = function(root) {
    if(!root)
    {
        return [];
    }
    return inorderTraversal(root.left).concat([root.val]).concat(inorderTraversal(root.right));
};