# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root, current_max = None):
        """
        :type root: TreeNode
        :rtype: int
        """

        if current_max == None:
            current_max = root.val

        if root == None :
            return 0
        
        new_max  = max(root.val, current_max)
    
        good_node = 1 if root.val >= current_max else 0

        if root.left:
            good_node += self.goodNodes(root.left, new_max)
            
        if root.right:
            good_node += self.goodNodes(root.right, new_max)
        
        return good_node
    

        
