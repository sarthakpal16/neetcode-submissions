/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int maxDepth(TreeNode* root) {

        if (root == nullptr){
            return 0;
        }
        
        int left = maxDepth(root->left);
        int right = maxDepth(root->right);
        int curr_max_depth = -1;
        if (left >= right) {
            curr_max_depth = left + 1;
        }
        else {
            curr_max_depth = right + 1;
        }
        
        return curr_max_depth;
    }
};
