class Solution(object):
    def isUnivalTree(self, root):
        def check(node,val):
            if not node:
                return True
            if node.val != val:
                return False
            return check(node.left,val) and check(node.right,val)
        
        return check(root,root.val)
        
