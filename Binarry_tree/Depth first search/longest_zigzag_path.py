# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def longestZigZag(self, root, dir="right"):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.max_length = 0

        if root.left== None and root.right == None:
            return 0

        if root == None:    
            return None
        
        def dfs(node, direction, lenght):
            if node == None:
                return 0
            
            self.max_length = max(self.max_length, lenght)
            if direction == "left":
                dfs(node.right, "right", lenght+1 )
                dfs(node.left, "left", 1)

            elif direction == "right":
                dfs(node.left, "left", lenght+1 )
                dfs(node.right, "right", 1)

        dfs(root.left, "right", 1 )
        dfs(root.right, "left", 1 )

        return self.max_length
