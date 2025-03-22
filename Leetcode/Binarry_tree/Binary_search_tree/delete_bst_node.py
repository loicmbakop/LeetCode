# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """

        if root == None:
            return None
        
        if key > root.val: # we are looking right
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val: # we are looking left
            root.left = self.deleteNode(root.left, key)
        
        else: # we are on th node to delete

            if root.left == None and root.right == None:
                return None
            
            elif root.left == None and root.right:
                return  root.right

            elif root.right == None and root.left:
                return root.left
            
            else:
                curr_node = root
                right_root = root.right
                while right_root.left:
                    right_root = right_root.left
                min_node_right = right_root
                root.val = min_node_right.val
                root.right = self.deleteNode(root.right, min_node_right.val)
            
            

                 

    


