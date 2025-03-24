
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if val == root.val:
            return root
        
        elif val > root.val: #check right side
            if root.right:
                root = root.right
            else:
                return None
        
        elif val < root.val: #check left side
            if root.left:
                root = root.left
            else:
                return None
                
        return self.searchBST(root, val)

    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        if root == None:
            return None
        
        if val == root.val:
            return root
        
        elif val > root.val: #check right side
            if root.right:
               return self.searchBST(root.right, val)
        
        elif val < root.val: #check left side
            if root.left:
               return self.searchBST(root.left, val)
                
       
        