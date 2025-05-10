class Solution {
public:
    bool check(TreeNode* node,int val){
        if(node == nullptr) return true;
        if(node->val != val) return false;
        return check(node->left, val) && check(node->right, val);
    }
    bool isUnivalTree(TreeNode* root) {
        return check(root,root->val);
    }
};
