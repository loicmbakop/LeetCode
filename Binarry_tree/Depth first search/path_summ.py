
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if root == None:
            return 0
        
        def dfs(node, target_sum):

            if node == None:
                return 0
            
            count = 1 if node.val == target_sum else 0

            count += dfs(node.right, target_sum - node.val)
            count+= dfs(node.left, target_sum - node.val)
            
            return count
        return(self.pathSum(root.left, targetSum) + dfs(root, targetSum) + self.pathSum(root.right, targetSum))