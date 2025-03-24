
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

       
        def get_leaves(root, leave):
            if root == None:
                return None
            
            if root.left == None and root.right == None:
                leave.append(root.val)

            get_leaves(root.left, leave)
            get_leaves(root.right, leave)
            return leave
        
        l1, l2 = [], []
        l1 = get_leaves(root1, l1)
        l2 = get_leaves(root2, l2)

        return l1 == l2
        