class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if(root == nullptr) return nullptr;
        if(root->val == val) return root;
        else if(val < root->val){
            return searchBST(root->left,val);
        }else if(val > root->val){
            return searchBST(root->right,val);
        }
        return 0;
    }
};
