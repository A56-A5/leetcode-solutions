class Solution {
    public boolean check(TreeNode node,int val){
        if(node == null) return true;
        if(node.val != val) return false;
        return check(node.left, val) && check(node.right, val);
    }
    public boolean isUnivalTree(TreeNode root) {
        return check(root,root.val);
    }
}
